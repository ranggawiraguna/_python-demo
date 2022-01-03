# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pageLogin.ui'
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
        self.widgetLogin = QtWidgets.QWidget(self.centralwidget)
        self.widgetLogin.setGeometry(QtCore.QRect(0, 0, 500, 500))
        self.widgetLogin.setMinimumSize(QtCore.QSize(500, 500))
        self.widgetLogin.setMaximumSize(QtCore.QSize(500, 500))
        self.widgetLogin.setObjectName("widgetLogin")
        self.background = QtWidgets.QLabel(self.widgetLogin)
        self.background.setGeometry(QtCore.QRect(0, 0, 500, 500))
        self.background.setMinimumSize(QtCore.QSize(500, 500))
        self.background.setMaximumSize(QtCore.QSize(500, 500))
        self.background.setText("")
        self.background.setPixmap(QtGui.QPixmap("../../TugasAkhir_Prolan/PageLogin/Background_Login.jpg"))
        self.background.setScaledContents(True)
        self.background.setObjectName("background")
        self.ShapesID = QtWidgets.QLabel(self.widgetLogin)
        self.ShapesID.setGeometry(QtCore.QRect(150, 180, 199, 29))
        self.ShapesID.setText("")
        self.ShapesID.setPixmap(QtGui.QPixmap("../../TugasAkhir_Prolan/PageLogin/P_ShapesID.png"))
        self.ShapesID.setScaledContents(True)
        self.ShapesID.setObjectName("ShapesID")
        self.ShapesPASS = QtWidgets.QLabel(self.widgetLogin)
        self.ShapesPASS.setGeometry(QtCore.QRect(150, 220, 199, 29))
        self.ShapesPASS.setText("")
        self.ShapesPASS.setPixmap(QtGui.QPixmap("../../TugasAkhir_Prolan/PageLogin/P_ShapesPWD.png"))
        self.ShapesPASS.setScaledContents(True)
        self.ShapesPASS.setObjectName("ShapesPASS")
        self.buttonLogin = QtWidgets.QToolButton(self.widgetLogin)
        self.buttonLogin.setGeometry(QtCore.QRect(210, 260, 91, 31))
        self.buttonLogin.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../../TugasAkhir_Prolan/PageLogin/P_ButtonLogin.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonLogin.setIcon(icon1)
        self.buttonLogin.setIconSize(QtCore.QSize(80, 23))
        self.buttonLogin.setAutoRaise(True)
        self.buttonLogin.setObjectName("buttonLogin")
        self.inputID = QtWidgets.QLineEdit(self.widgetLogin)
        self.inputID.setGeometry(QtCore.QRect(214, 184, 127, 20))
        self.inputID.setObjectName("inputID")
        self.inputPASS = QtWidgets.QLineEdit(self.widgetLogin)
        self.inputPASS.setGeometry(QtCore.QRect(214, 224, 127, 20))
        self.inputPASS.setObjectName("inputPASS")
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
