# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1086, 676)
        MainWindow.setAnimated(False)
        MainWindow.setDocumentMode(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Uncurate_box = QtWidgets.QGroupBox(self.centralwidget)
        self.Uncurate_box.setGeometry(QtCore.QRect(40, 60, 291, 411))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Uncurate_box.setFont(font)
        self.Uncurate_box.setFlat(False)
        self.Uncurate_box.setObjectName("Uncurate_box")
        self.Un_edit = QtWidgets.QTextEdit(self.Uncurate_box)
        self.Un_edit.setGeometry(QtCore.QRect(70, 100, 131, 81))
        self.Un_edit.setObjectName("Un_edit")
        self.Unc_show_btn = QtWidgets.QPushButton(self.Uncurate_box)
        self.Unc_show_btn.setGeometry(QtCore.QRect(80, 270, 111, 31))
        self.Unc_show_btn.setObjectName("Unc_show_btn")
        self.Style_box = QtWidgets.QGroupBox(self.centralwidget)
        self.Style_box.setGeometry(QtCore.QRect(390, 60, 581, 411))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Style_box.setFont(font)
        self.Style_box.setFlat(False)
        self.Style_box.setObjectName("Style_box")
        self.Dst3_edit = QtWidgets.QTextEdit(self.Style_box)
        self.Dst3_edit.setGeometry(QtCore.QRect(50, 250, 91, 41))
        self.Dst3_edit.setObjectName("Dst3_edit")
        self.Style_show_btn = QtWidgets.QPushButton(self.Style_box)
        self.Style_show_btn.setGeometry(QtCore.QRect(250, 320, 171, 31))
        self.Style_show_btn.setObjectName("Style_show_btn")
        self.Dst2_edit = QtWidgets.QTextEdit(self.Style_box)
        self.Dst2_edit.setGeometry(QtCore.QRect(50, 170, 91, 41))
        self.Dst2_edit.setObjectName("Dst2_edit")
        self.Dst1_edit = QtWidgets.QTextEdit(self.Style_box)
        self.Dst1_edit.setGeometry(QtCore.QRect(50, 90, 91, 41))
        self.Dst1_edit.setObjectName("Dst1_edit")
        self.Src1_edit = QtWidgets.QTextEdit(self.Style_box)
        self.Src1_edit.setGeometry(QtCore.QRect(180, 30, 91, 41))
        self.Src1_edit.setObjectName("Src1_edit")
        self.Src3_edit = QtWidgets.QTextEdit(self.Style_box)
        self.Src3_edit.setGeometry(QtCore.QRect(420, 30, 91, 41))
        self.Src3_edit.setObjectName("Src3_edit")
        self.Src2_edit = QtWidgets.QTextEdit(self.Style_box)
        self.Src2_edit.setGeometry(QtCore.QRect(300, 30, 91, 41))
        self.Src2_edit.setObjectName("Src2_edit")
        self.Range_lab = QtWidgets.QLabel(self.centralwidget)
        self.Range_lab.setGeometry(QtCore.QRect(730, 480, 241, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Range_lab.setFont(font)
        self.Range_lab.setObjectName("Range_lab")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1086, 25))
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
        self.Uncurate_box.setTitle(_translate("MainWindow", "Uncurated"))
        self.Unc_show_btn.setText(_translate("MainWindow", "Show"))
        self.Style_box.setTitle(_translate("MainWindow", "Style Mixing"))
        self.Style_show_btn.setText(_translate("MainWindow", "Show"))
        self.Range_lab.setText(_translate("MainWindow", "Input must between 0~2^32-1"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
