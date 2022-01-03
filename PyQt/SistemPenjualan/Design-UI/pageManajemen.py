# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pageManajemen.ui'
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
        self.Frame.setPixmap(QtGui.QPixmap("../mainApplication/Picture/FrameManajemen.jpg"))
        self.Frame.setScaledContents(True)
        self.Frame.setObjectName("Frame")
        self.buttonPenjualan = QtWidgets.QToolButton(self.widget)
        self.buttonPenjualan.setGeometry(QtCore.QRect(160, 186, 180, 31))
        self.buttonPenjualan.setMinimumSize(QtCore.QSize(180, 31))
        self.buttonPenjualan.setMaximumSize(QtCore.QSize(180, 31))
        self.buttonPenjualan.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.buttonPenjualan.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../mainApplication/Picture/buttonDataPenjualan.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonPenjualan.setIcon(icon1)
        self.buttonPenjualan.setIconSize(QtCore.QSize(180, 31))
        self.buttonPenjualan.setAutoRaise(True)
        self.buttonPenjualan.setObjectName("buttonPenjualan")
        self.buttonPenjualan_2 = QtWidgets.QToolButton(self.widget)
        self.buttonPenjualan_2.setGeometry(QtCore.QRect(160, 249, 180, 31))
        self.buttonPenjualan_2.setMinimumSize(QtCore.QSize(180, 31))
        self.buttonPenjualan_2.setMaximumSize(QtCore.QSize(180, 31))
        self.buttonPenjualan_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.buttonPenjualan_2.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../mainApplication/Picture/buttonDataTerjual.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonPenjualan_2.setIcon(icon2)
        self.buttonPenjualan_2.setIconSize(QtCore.QSize(180, 31))
        self.buttonPenjualan_2.setAutoRaise(True)
        self.buttonPenjualan_2.setObjectName("buttonPenjualan_2")
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
