from PyQt5 import QtCore, QtGui, QtWidgets

def pageLogin(self):

    self.pageLogin = dict()
    self.pageLogin["widget"] = QtWidgets.QWidget(self.centralwidget)
    self.pageLogin["widget"].setGeometry(QtCore.QRect(0, 0, 500, 500))
    self.pageLogin["widget"].setMinimumSize(QtCore.QSize(500, 500))
    self.pageLogin["widget"].setMaximumSize(QtCore.QSize(500, 500))

    self.pageLogin["background"] = QtWidgets.QLabel(self.pageLogin["widget"])
    self.pageLogin["background"].setGeometry(QtCore.QRect(0, 0, 500, 500))
    self.pageLogin["background"].setMinimumSize(QtCore.QSize(500, 500))
    self.pageLogin["background"].setMaximumSize(QtCore.QSize(500, 500))
    self.pageLogin["background"].setText("")
    self.pageLogin["background"].setPixmap(QtGui.QPixmap("Picture/Background_Login.jpg"))
    self.pageLogin["background"].setScaledContents(True)

    self.pageLogin["ShapesID"] = QtWidgets.QLabel(self.pageLogin["widget"])
    self.pageLogin["ShapesID"].setGeometry(QtCore.QRect(150, 180, 199, 29))
    self.pageLogin["ShapesID"].setText("")
    self.pageLogin["ShapesID"].setPixmap(QtGui.QPixmap("Picture/P_ShapesID.png"))
    self.pageLogin["ShapesID"].setScaledContents(True)

    self.pageLogin["ShapesPASS"] = QtWidgets.QLabel(self.pageLogin["widget"])
    self.pageLogin["ShapesPASS"].setGeometry(QtCore.QRect(150, 220, 199, 29))
    self.pageLogin["ShapesPASS"].setText("")
    self.pageLogin["ShapesPASS"].setPixmap(QtGui.QPixmap("Picture/P_ShapesPWD.png"))
    self.pageLogin["ShapesPASS"].setScaledContents(True)

    self.pageLogin["buttonLogin"] = QtWidgets.QToolButton(self.pageLogin["widget"])
    self.pageLogin["buttonLogin"].setGeometry(QtCore.QRect(210, 260, 91, 31))
    self.pageLogin["buttonLogin"].setText("")
    icon1 = QtGui.QIcon()
    icon1.addPixmap(QtGui.QPixmap("Picture/P_ButtonLogin.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    self.pageLogin["buttonLogin"].setIcon(icon1)
    self.pageLogin["buttonLogin"].setIconSize(QtCore.QSize(80, 23))
    self.pageLogin["buttonLogin"].setAutoRaise(True)

    self.pageLogin["inputID"] = QtWidgets.QLineEdit(self.pageLogin["widget"])
    self.pageLogin["inputID"].setGeometry(QtCore.QRect(214, 184, 127, 20))

    self.pageLogin["inputPASS"] = QtWidgets.QLineEdit(self.pageLogin["widget"])
    self.pageLogin["inputPASS"].setGeometry(QtCore.QRect(214, 224, 127, 20))
    self.pageLogin["inputPASS"].setEchoMode(QtWidgets.QLineEdit.Password)

    self.pageLogin["Notice"] = QtWidgets.QLabel(self.pageLogin["widget"])
    self.pageLogin["Notice"].setGeometry(QtCore.QRect(150, 298, 200, 41))
    font = QtGui.QFont()
    font.setPointSize(9)
    self.pageLogin["Notice"].setFont(font)
    self.pageLogin["Notice"].setText("")
    self.pageLogin["Notice"].setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
