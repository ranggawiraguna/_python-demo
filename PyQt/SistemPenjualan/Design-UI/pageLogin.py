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
        self.Frame.setPixmap(QtGui.QPixmap("../mainApplication/Picture/FrameLogin.jpg"))
        self.Frame.setScaledContents(True)
        self.Frame.setObjectName("Frame")
        self.inputKey = QtWidgets.QLineEdit(self.widget)
        self.inputKey.setGeometry(QtCore.QRect(153, 211, 192, 24))
        self.inputKey.setMinimumSize(QtCore.QSize(192, 24))
        self.inputKey.setMaximumSize(QtCore.QSize(192, 24))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.inputKey.setFont(font)
        self.inputKey.setMaxLength(15)
        self.inputKey.setFrame(False)
        self.inputKey.setEchoMode(QtWidgets.QLineEdit.Password)
        self.inputKey.setAlignment(QtCore.Qt.AlignCenter)
        self.inputKey.setObjectName("inputKey")
        self.buttonLogin = QtWidgets.QToolButton(self.widget)
        self.buttonLogin.setGeometry(QtCore.QRect(217, 253, 69, 28))
        self.buttonLogin.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.buttonLogin.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../mainApplication/Picture/buttonLogin.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonLogin.setIcon(icon1)
        self.buttonLogin.setIconSize(QtCore.QSize(66, 26))
        self.buttonLogin.setAutoRaise(True)
        self.buttonLogin.setObjectName("buttonLogin")
        self.notice = QtWidgets.QLabel(self.widget)
        self.notice.setGeometry(QtCore.QRect(156, 300, 185, 81))
        self.notice.setMinimumSize(QtCore.QSize(185, 81))
        self.notice.setMaximumSize(QtCore.QSize(185, 81))
        self.notice.setText("")
        self.notice.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.notice.setObjectName("notice")
        self.toolButton = QtWidgets.QToolButton(self.widget)
        self.toolButton.setGeometry(QtCore.QRect(313, 213, 29, 19))
        self.toolButton.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../mainApplication/Picture/iconHideEcho.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton.setIcon(icon2)
        self.toolButton.setIconSize(QtCore.QSize(29, 22))
        self.toolButton.setAutoRaise(True)
        self.toolButton.setObjectName("toolButton")
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
