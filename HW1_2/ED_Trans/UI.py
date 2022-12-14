# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(612, 431)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Img_btn = QtWidgets.QPushButton(self.centralwidget)
        self.Img_btn.setGeometry(QtCore.QRect(30, 150, 111, 31))
        self.Img_btn.setObjectName("Img_btn")
        self.Img_lab = QtWidgets.QLabel(self.centralwidget)
        self.Img_lab.setGeometry(QtCore.QRect(30, 190, 111, 21))
        self.Img_lab.setObjectName("Img_lab")
        self.Edge_box = QtWidgets.QGroupBox(self.centralwidget)
        self.Edge_box.setGeometry(QtCore.QRect(180, 30, 181, 341))
        self.Edge_box.setObjectName("Edge_box")
        self.Gau_Blur_btn = QtWidgets.QPushButton(self.Edge_box)
        self.Gau_Blur_btn.setGeometry(QtCore.QRect(20, 50, 141, 31))
        self.Gau_Blur_btn.setObjectName("Gau_Blur_btn")
        self.Sol_X_btn = QtWidgets.QPushButton(self.Edge_box)
        self.Sol_X_btn.setGeometry(QtCore.QRect(20, 110, 141, 31))
        self.Sol_X_btn.setObjectName("Sol_X_btn")
        self.Sol_Y_btn = QtWidgets.QPushButton(self.Edge_box)
        self.Sol_Y_btn.setGeometry(QtCore.QRect(20, 180, 141, 31))
        self.Sol_Y_btn.setObjectName("Sol_Y_btn")
        self.Mag_btn = QtWidgets.QPushButton(self.Edge_box)
        self.Mag_btn.setGeometry(QtCore.QRect(20, 250, 141, 31))
        self.Mag_btn.setObjectName("Mag_btn")
        self.Trans_box = QtWidgets.QGroupBox(self.centralwidget)
        self.Trans_box.setGeometry(QtCore.QRect(380, 30, 191, 341))
        self.Trans_box.setObjectName("Trans_box")
        self.Res_btn = QtWidgets.QPushButton(self.Trans_box)
        self.Res_btn.setGeometry(QtCore.QRect(30, 50, 141, 31))
        self.Res_btn.setObjectName("Res_btn")
        self.Tran_btn = QtWidgets.QPushButton(self.Trans_box)
        self.Tran_btn.setGeometry(QtCore.QRect(30, 110, 141, 31))
        self.Tran_btn.setObjectName("Tran_btn")
        self.Rot_Scal_btn = QtWidgets.QPushButton(self.Trans_box)
        self.Rot_Scal_btn.setGeometry(QtCore.QRect(30, 180, 141, 31))
        self.Rot_Scal_btn.setObjectName("Rot_Scal_btn")
        self.Shea_btn = QtWidgets.QPushButton(self.Trans_box)
        self.Shea_btn.setGeometry(QtCore.QRect(30, 250, 141, 31))
        self.Shea_btn.setObjectName("Shea_btn")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 612, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Img_btn.setText(_translate("MainWindow", "Load Image"))
        self.Img_lab.setText(_translate("MainWindow", "TextLabel"))
        self.Edge_box.setTitle(_translate("MainWindow", "3. Edge Dectection"))
        self.Gau_Blur_btn.setText(_translate("MainWindow", "3.1 Gaussian Blur"))
        self.Sol_X_btn.setText(_translate("MainWindow", "3.2 Sobel X"))
        self.Sol_Y_btn.setText(_translate("MainWindow", "3.3 Sobel Y"))
        self.Mag_btn.setText(_translate("MainWindow", "3.4 Magnitude"))
        self.Trans_box.setTitle(_translate("MainWindow", "4. Transformation"))
        self.Res_btn.setText(_translate("MainWindow", "4.1 Resize"))
        self.Tran_btn.setText(_translate("MainWindow", "4.2 Translation"))
        self.Rot_Scal_btn.setText(_translate("MainWindow", "4.3 Rotation, Scaling"))
        self.Shea_btn.setText(_translate("MainWindow", "4.4 Shearing"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
