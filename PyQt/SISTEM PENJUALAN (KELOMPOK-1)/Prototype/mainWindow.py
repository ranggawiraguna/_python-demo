from PyQt5 import QtCore, QtGui, QtWidgets

from Prototype.pageDaftar import *
from Prototype.pageLogin import *
from Prototype.pageManajemen import *
from Prototype.pageOperasiPenjualan import *
from Prototype.pageOperasiTerjual import *
from Prototype.pageInputDataPenjualan import *
from Prototype.pageInputDataTerjual import *
from Prototype.pageLihatDataPenjualan import *
from Prototype.pageLihatDataTerjual import *
from Prototype.pageDeleteDataPenjualan import *
from Prototype.pageDeleteDataTerjual import *
from Prototype.clearPageApp import *
from Prototype.operasiFile_Database import *

class Ui_MainWindow(object):
    status = False
    def setupUi(self, MainWindow, widget):

        MainWindow.resize(500, 500)
        MainWindow.setMinimumSize(QtCore.QSize(500, 500))
        MainWindow.setMaximumSize(QtCore.QSize(500, 500))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Picture/WindowIcon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)

        if widget is "pageDaftar" : pageDaftar(self)
        elif widget is "pageLogin" : pageLogin(self)
        elif widget is "pageManajemen" : pageManajemen(self)
        elif widget is "pageOperasiPenjualan" : pageOperasiPenjualan(self)
        elif widget is "pageOperasiTerjual" : pageOperasiTerjual(self)
        elif widget is "pageInputDataPenjualan" : pageInputDataPenjualan(self)
        elif widget is "pageInputDataTerjual" : pageInputDataTerjual(self)
        elif widget is "pageLihatDataPenjualan" : pageLihatDataPenjualan(self)
        elif widget is "pageLihatDataTerjual" : pageLihatDataTerjual(self)
        elif widget is "pageDeleteDataPenjualan" : pageDeleteDataPenjualan(self)
        elif widget is "pageDeleteDataTerjual" : pageDeleteDataTerjual(self)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.status = True

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Manajemen Perdagangan"))


if __name__ == "__main__" :
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow, "pageDeleteDataTerjual")
    MainWindow.show()
    sys.exit(app.exec_())
