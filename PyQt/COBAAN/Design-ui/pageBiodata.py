# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pageBiodata.ui'
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
        self.background = QtWidgets.QLabel(self.widget)
        self.background.setGeometry(QtCore.QRect(0, 0, 500, 500))
        self.background.setMinimumSize(QtCore.QSize(500, 500))
        self.background.setMaximumSize(QtCore.QSize(500, 500))
        self.background.setText("")
        self.background.setPixmap(QtGui.QPixmap("E:/Rangga Wiraguna/500px/Design/Sample/OQCI8X0.jpg"))
        self.background.setScaledContents(True)
        self.background.setObjectName("background")
        self.input_A = QtWidgets.QLineEdit(self.widget)
        self.input_A.setGeometry(QtCore.QRect(140, 90, 271, 21))
        self.input_A.setObjectName("input_A")
        self.input_B = QtWidgets.QLineEdit(self.widget)
        self.input_B.setGeometry(QtCore.QRect(140, 150, 271, 21))
        self.input_B.setObjectName("input_B")
        self.input_C = QtWidgets.QLineEdit(self.widget)
        self.input_C.setGeometry(QtCore.QRect(140, 210, 271, 21))
        self.input_C.setObjectName("input_C")
        self.input_D = QtWidgets.QLineEdit(self.widget)
        self.input_D.setGeometry(QtCore.QRect(140, 270, 271, 21))
        self.input_D.setObjectName("input_D")
        self.input_E = QtWidgets.QLineEdit(self.widget)
        self.input_E.setGeometry(QtCore.QRect(140, 330, 271, 21))
        self.input_E.setObjectName("input_E")
        self.toolButton = QtWidgets.QToolButton(self.widget)
        self.toolButton.setGeometry(QtCore.QRect(210, 370, 91, 31))
        self.toolButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("E:/Rangga Wiraguna/500px/Design/Project-1/Page1_Login/ExctractLayout/P_buttonSave.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton.setIcon(icon1)
        self.toolButton.setIconSize(QtCore.QSize(80, 23))
        self.toolButton.setAutoRaise(True)
        self.toolButton.setObjectName("toolButton")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(60, 85, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(60, 144, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(60, 205, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setGeometry(QtCore.QRect(60, 264, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setGeometry(QtCore.QRect(60, 324, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "APLIKASI COBAAN"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Nama</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Alamat</span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">TTL</span></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Agama</span></p></body></html>"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Hobi</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
