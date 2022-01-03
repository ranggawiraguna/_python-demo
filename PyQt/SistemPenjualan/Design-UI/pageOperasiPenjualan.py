# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pageOperasiPenjualan.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 500)
        MainWindow.setMinimumSize(QtCore.QSize(500, 500))
        MainWindow.setMaximumSize(QtCore.QSize(500, 500))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../TugasAkhir_Prolan/PageLogin/P_Icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(0, 0, 500, 500))
        self.widget.setMinimumSize(QtCore.QSize(500, 500))
        self.widget.setMaximumSize(QtCore.QSize(500, 500))
        self.widget.setObjectName("widget")
        self.Frame = QtWidgets.QLabel(self.widget)
        self.Frame.setGeometry(QtCore.QRect(0, 0, 500, 500))
        self.Frame.setMinimumSize(QtCore.QSize(500, 500))
        self.Frame.setMaximumSize(QtCore.QSize(500, 500))
        self.Frame.setText("")
        self.Frame.setPixmap(QtGui.QPixmap("../mainApplication/Picture/FrameDataPenjualan.jpg"))
        self.Frame.setScaledContents(True)
        self.Frame.setObjectName("Frame")
        self.buttonView = QtWidgets.QToolButton(self.widget)
        self.buttonView.setGeometry(QtCore.QRect(160, 199, 180, 32))
        self.buttonView.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.buttonView.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../mainApplication/Picture/buttonViewData.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonView.setIcon(icon1)
        self.buttonView.setIconSize(QtCore.QSize(174, 28))
        self.buttonView.setAutoRaise(True)
        self.buttonView.setObjectName("buttonView")
        self.buttonInput = QtWidgets.QToolButton(self.widget)
        self.buttonInput.setGeometry(QtCore.QRect(160, 261, 181, 31))
        self.buttonInput.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.buttonInput.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../mainApplication/Picture/buttonInputData.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonInput.setIcon(icon2)
        self.buttonInput.setIconSize(QtCore.QSize(175, 33))
        self.buttonInput.setAutoRaise(True)
        self.buttonInput.setObjectName("buttonInput")
        self.buttonUpdate = QtWidgets.QToolButton(self.widget)
        self.buttonUpdate.setGeometry(QtCore.QRect(160, 320, 180, 32))
        self.buttonUpdate.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.buttonUpdate.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("../mainApplication/Picture/buttonUpdateData.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonUpdate.setIcon(icon3)
        self.buttonUpdate.setIconSize(QtCore.QSize(174, 28))
        self.buttonUpdate.setAutoRaise(True)
        self.buttonUpdate.setObjectName("buttonUpdate")
        self.buttonBack = QtWidgets.QToolButton(self.widget)
        self.buttonBack.setGeometry(QtCore.QRect(204, 367, 95, 35))
        self.buttonBack.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.buttonBack.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("../mainApplication/Picture/buttonBack.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonBack.setIcon(icon4)
        self.buttonBack.setIconSize(QtCore.QSize(97, 38))
        self.buttonBack.setAutoRaise(True)
        self.buttonBack.setObjectName("buttonBack")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "APLIKASI COBAAN"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
