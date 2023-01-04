from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QFileDialog
from UI import Ui_MainWindow
from generate_figures import call_uncreated, call_style
import os
import pickle
import numpy as np
import PIL.Image
import dnnlib
import dnnlib.tflib as tflib
import config


class MainWindow_controller(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setup_control()
        self.url_ffhq          = './karras2019stylegan-ffhq-1024x1024.pkl' # 'https://drive.google.com/uc?id=1MEGjdvVpUsu1jB4zrXZN7Y4kBBOzizDQ'
        self.synthesis_kwargs = dict(output_transform=dict(func=tflib.convert_images_to_uint8, nchw_to_nhwc=True), minibatch_size=8)
        self._Gs_cache = dict()

    def setup_control(self):
        self.ui.Unc_show_btn.clicked.connect(lambda: self.call_uncreated(int(self.ui.Un_edit.toPlainText())))
        self.ui.Style_show_btn.clicked.connect(lambda: self.call_style(int(self.ui.Src1_edit.toPlainText()), 
                                                    int(self.ui.Src2_edit.toPlainText()), 
                                                    int(self.ui.Src3_edit.toPlainText()), 
                                                    int(self.ui.Dst1_edit.toPlainText()), 
                                                    int(self.ui.Dst2_edit.toPlainText()), 
                                                    int(self.ui.Dst3_edit.toPlainText())))


    def load_Gs(self, url):
        if url not in self._Gs_cache:
            # with dnnlib.util.open_url(url, cache_dir=config.cache_dir) as f:
            #     _G, _D, Gs = pickle.load(f)
            # _Gs_cache[url] = Gs
            with open(url, 'rb') as f:
                _G, _D, Gs = pickle.load(f)
            self._Gs_cache[url] = Gs
        return self._Gs_cache[url]

    #----------------------------------------------------------------------------
    # Figures 2, 3, 10, 11, 12: Multi-resolution grid of uncurated result images.

    def draw_uncurated_result_figure(self, png, Gs, cx, cy, cw, ch, rows, lods, seed):
        latents = np.random.RandomState(seed).randn(sum(rows * 2**lod for lod in lods), Gs.input_shape[1])
        images = Gs.run(latents, None, **self.synthesis_kwargs) # [seed, y, x, rgb]

        canvas = PIL.Image.new('RGB', (sum(cw // 2**lod for lod in lods), ch * rows), 'white')
        image_iter = iter(list(images))
        for col, lod in enumerate(lods):
            for row in range(rows * 2**lod):
                image = PIL.Image.fromarray(next(image_iter), 'RGB')
                image = image.crop((cx, cy, cx + cw, cy + ch))
                image = image.resize((cw // 2**lod, ch // 2**lod), PIL.Image.ANTIALIAS)
                canvas.paste(image, (sum(cw // 2**lod for lod in lods[:col]), row * ch // 2**lod))
        canvas.show()
        canvas.save(png)

    #----------------------------------------------------------------------------
    # Figure 3: Style mixing.

    def draw_style_mixing_figure(self, png, Gs, w, h, src_seeds, dst_seeds, style_ranges):
        # print(png)
        src_latents = np.stack(np.random.RandomState(seed).randn(Gs.input_shape[1]) for seed in src_seeds)
        dst_latents = np.stack(np.random.RandomState(seed).randn(Gs.input_shape[1]) for seed in dst_seeds)
        src_dlatents = Gs.components.mapping.run(src_latents, None) # [seed, layer, component]
        dst_dlatents = Gs.components.mapping.run(dst_latents, None) # [seed, layer, component]
        src_images = Gs.components.synthesis.run(src_dlatents, randomize_noise=False, **self.synthesis_kwargs)
        dst_images = Gs.components.synthesis.run(dst_dlatents, randomize_noise=False, **self.synthesis_kwargs)
        canvas = PIL.Image.new('RGB', (w * (len(src_seeds) + 1), h * (len(dst_seeds) + 1)), 'white')
        for col, src_image in enumerate(list(src_images)):
            canvas.paste(PIL.Image.fromarray(src_image, 'RGB'), ((col + 1) * w, 0))
        for row, dst_image in enumerate(list(dst_images)):
            canvas.paste(PIL.Image.fromarray(dst_image, 'RGB'), (0, (row + 1) * h))

            row_dlatents = np.stack([dst_dlatents[row]] * len(src_seeds))
            row_dlatents[:, style_ranges[row]] = src_dlatents[:, style_ranges[row]]
            row_images = Gs.components.synthesis.run(row_dlatents, randomize_noise=False, **self.synthesis_kwargs)
            for col, image in enumerate(list(row_images)):
                canvas.paste(PIL.Image.fromarray(image, 'RGB'), ((col + 1) * w, (row + 1) * h))
        canvas.show()
        canvas.save(png)

    #----------------------------------------------------------------------------
    # Main program.

    def call_uncreated(self, seed):
        if seed > 2**32: seed = 87
        tflib.init_tf()
        os.makedirs(config.result_dir, exist_ok=True)
        self.draw_uncurated_result_figure(os.path.join(config.result_dir, 'figure02-uncurated-ffhq.png'), self.load_Gs(self.url_ffhq), cx=0, cy=0, cw=1024, ch=1024, rows=3, lods=[0], seed=seed) # ,1,2,2,3,3

    def call_style(self, src1, src2, src3, dst1, dst2, dst3):
        if src1 > 2**32: src1 = 87
        if src2 > 2**32: src2 = 87
        if src3 > 2**32: src3 = 87
        if dst1 > 2**32: dst1 = 87
        if dst2 > 2**32: dst2 = 87
        if dst3 > 2**32: dst3 = 87
        tflib.init_tf()
        os.makedirs(config.result_dir, exist_ok=True)  
        self.draw_style_mixing_figure(os.path.join(config.result_dir, 'figure03-style-mixing.png'), self.load_Gs(self.url_ffhq), w=1024, h=1024, src_seeds=[src1, src2, src3], dst_seeds=[dst1, dst2, dst3], style_ranges=[range(0,4)]*1+[range(4,8)]*1+[range(8,18)]*1) # ,615,2268 ; ,1733,1614,845
    