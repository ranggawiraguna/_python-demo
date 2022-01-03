# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pageLihatDataPenjualan.ui'
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
        self.Frame.setText("")
        self.Frame.setPixmap(QtGui.QPixmap("../mainApplication/Picture/FrameLihatDataPenjualan.jpg"))
        self.Frame.setScaledContents(True)
        self.Frame.setObjectName("Frame")
        self.TabelData = QtWidgets.QTableWidget(self.widget)
        self.TabelData.setGeometry(QtCore.QRect(51, 101, 400, 271))
        self.TabelData.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.TabelData.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.TabelData.setAlternatingRowColors(True)
        self.TabelData.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.TabelData.setRowCount(10)
        self.TabelData.setObjectName("TabelData")
        self.TabelData.setColumnCount(4)
        item = QtWidgets.QTableWidgetItem()
        self.TabelData.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.TabelData.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.TabelData.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.TabelData.setHorizontalHeaderItem(3, item)
        self.TabelData.horizontalHeader().setDefaultSectionSize(94)
        self.TabelData.horizontalHeader().setMinimumSectionSize(98)
        self.TabelData.verticalHeader().setCascadingSectionResizes(True)
        self.TabelData.verticalHeader().setDefaultSectionSize(20)
        self.TabelData.verticalHeader().setMinimumSectionSize(20)
        self.buttonUnduh = QtWidgets.QToolButton(self.widget)
        self.buttonUnduh.setGeometry(QtCore.QRect(238, 380, 31, 31))
        self.buttonUnduh.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.buttonUnduh.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../mainApplication/Picture/iconUnduh.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonUnduh.setIcon(icon1)
        self.buttonUnduh.setIconSize(QtCore.QSize(100, 100))
        self.buttonUnduh.setAutoRaise(True)
        self.buttonUnduh.setObjectName("buttonUnduh")
        self.Teks = QtWidgets.QLabel(self.widget)
        self.Teks.setGeometry(QtCore.QRect(237, 410, 41, 16))
        self.Teks.setObjectName("Teks")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(76, 440, 351, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setText("")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "APLIKASI COBAAN"))
        item = self.TabelData.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Kode Barang"))
        item = self.TabelData.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Nama Barang"))
        item = self.TabelData.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Jumlah Barang"))
        item = self.TabelData.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Keterangan"))
        self.Teks.setText(_translate("MainWindow", "UNDUH"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
