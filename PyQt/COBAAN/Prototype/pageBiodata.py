from PyQt5 import QtCore, QtGui, QtWidgets

def pageBiodata(self):
    self.pageBiodata = dict()
    self.pageBiodata["widget"] = QtWidgets.QWidget(self.centralwidget)
    self.pageBiodata["widget"].setGeometry(QtCore.QRect(0, 0, 500, 500))
    self.pageBiodata["widget"].setMinimumSize(QtCore.QSize(500, 500))
    self.pageBiodata["widget"].setMaximumSize(QtCore.QSize(500, 500))

    self.pageBiodata["background"] = QtWidgets.QLabel(self.pageBiodata["widget"])
    self.pageBiodata["background"].setGeometry(QtCore.QRect(0, 0, 500, 500))
    self.pageBiodata["background"].setMinimumSize(QtCore.QSize(500, 500))
    self.pageBiodata["background"].setMaximumSize(QtCore.QSize(500, 500))
    self.pageBiodata["background"].setText("")
    self.pageBiodata["background"].setPixmap(QtGui.QPixmap("Picture/Background_Biodata.jpg"))
    self.pageBiodata["background"].setScaledContents(True)

    self.pageBiodata["input_A"] = QtWidgets.QLineEdit(self.pageBiodata["widget"])
    self.pageBiodata["input_A"].setGeometry(QtCore.QRect(140, 90, 271, 21))

    self.pageBiodata["input_B"] = QtWidgets.QLineEdit(self.pageBiodata["widget"])
    self.pageBiodata["input_B"].setGeometry(QtCore.QRect(140, 150, 271, 21))

    self.pageBiodata["input_C"] = QtWidgets.QLineEdit(self.pageBiodata["widget"])
    self.pageBiodata["input_C"].setGeometry(QtCore.QRect(140, 210, 271, 21))

    self.pageBiodata["input_D"] = QtWidgets.QLineEdit(self.pageBiodata["widget"])
    self.pageBiodata["input_D"].setGeometry(QtCore.QRect(140, 270, 271, 21))

    self.pageBiodata["input_E"] = QtWidgets.QLineEdit(self.pageBiodata["widget"])
    self.pageBiodata["input_E"].setGeometry(QtCore.QRect(140, 330, 271, 21))

    self.pageBiodata["toolButton"] = QtWidgets.QToolButton(self.pageBiodata["widget"])
    self.pageBiodata["toolButton"].setGeometry(QtCore.QRect(210, 370, 91, 31))
    self.pageBiodata["toolButton"].setText("")
    icon1 = QtGui.QIcon()
    icon1.addPixmap(QtGui.QPixmap("Picture/P_buttonSave.png"),QtGui.QIcon.Normal, QtGui.QIcon.Off)
    self.pageBiodata["toolButton"].setIcon(icon1)
    self.pageBiodata["toolButton"].setIconSize(QtCore.QSize(80, 23))
    self.pageBiodata["toolButton"].setAutoRaise(True)

    self.pageBiodata["Label1"] = QtWidgets.QLabel(self.pageBiodata["widget"])
    self.pageBiodata["Label1"].setGeometry(QtCore.QRect(60, 85, 71, 31))
    font = QtGui.QFont()
    font.setPointSize(14)
    self.pageBiodata["Label1"].setFont(font)

    self.pageBiodata["Label2"] = QtWidgets.QLabel(self.pageBiodata["widget"])
    self.pageBiodata["Label2"].setGeometry(QtCore.QRect(60, 144, 71, 31))
    font = QtGui.QFont()
    font.setPointSize(14)
    self.pageBiodata["Label2"].setFont(font)

    self.pageBiodata["Label3"] = QtWidgets.QLabel(self.pageBiodata["widget"])
    self.pageBiodata["Label3"].setGeometry(QtCore.QRect(60, 205, 71, 31))
    font = QtGui.QFont()
    font.setPointSize(14)
    self.pageBiodata["Label3"].setFont(font)

    self.pageBiodata["Label4"] = QtWidgets.QLabel(self.pageBiodata["widget"])
    self.pageBiodata["Label4"].setGeometry(QtCore.QRect(60, 264, 71, 31))
    font = QtGui.QFont()
    font.setPointSize(14)
    self.pageBiodata["Label4"].setFont(font)

    self.pageBiodata["Label5"] = QtWidgets.QLabel(self.pageBiodata["widget"])
    self.pageBiodata["Label5"].setGeometry(QtCore.QRect(60, 324, 71, 31))
    font = QtGui.QFont()
    font.setPointSize(14)
    self.pageBiodata["Label5"].setFont(font)

    _translate = QtCore.QCoreApplication.translate
    self.pageBiodata["Label1"].setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Nama</span></p></body></html>"))
    self.pageBiodata["Label2"].setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Alamat</span></p></body></html>"))
    self.pageBiodata["Label3"].setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">TTL</span></p></body></html>"))
    self.pageBiodata["Label4"].setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Agama</span></p></body></html>"))
    self.pageBiodata["Label5"].setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Hobi</span></p></body></html>"))

