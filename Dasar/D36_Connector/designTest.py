# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'designTest.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 500)
        MainWindow.setMinimumSize(QtCore.QSize(400, 500))
        MainWindow.setMaximumSize(QtCore.QSize(400, 500))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.background = QtWidgets.QLabel(self.centralwidget)
        self.background.setGeometry(QtCore.QRect(0, 0, 400, 500))
        self.background.setText("")
        self.background.setPixmap(QtGui.QPixmap("Chatting_L.png"))
        self.background.setObjectName("background")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(10, 50, 380, 400))
        self.scrollArea.setMinimumSize(QtCore.QSize(380, 400))
        self.scrollArea.setMaximumSize(QtCore.QSize(380, 16777215))
        self.scrollArea.setStyleSheet("background-color:transparent;")
        self.scrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea.setFrameShadow(QtWidgets.QFrame.Raised)
        self.scrollArea.setWidgetResizable(False)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 380, 400))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.label_A = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_A.setGeometry(QtCore.QRect(40, 20, 300, 30))
        self.label_A.setMinimumSize(QtCore.QSize(24, 24))
        self.label_A.setMaximumSize(QtCore.QSize(300, 16777215))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB")
        font.setPointSize(9)
        self.label_A.setFont(font)
        self.label_A.setStyleSheet("background-color : rgb(220, 139, 45);\n"
"border-style : outset;\n"
"border-width : 2px;\n"
"border-radius : 10px;\n"
"border-color : gray;\n"
"min-height : 20px;\n"
"min-width : 20px;\n"
"color : white;\n"
"")
        self.label_A.setFrameShape(QtWidgets.QFrame.Box)
        self.label_A.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_A.setLineWidth(20)
        self.label_A.setMidLineWidth(0)
        self.label_A.setIndent(10)
        self.label_A.setObjectName("label_A")
        self.label_A_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_A_2.setGeometry(QtCore.QRect(40, 55, 300, 30))
        self.label_A_2.setMinimumSize(QtCore.QSize(24, 24))
        self.label_A_2.setMaximumSize(QtCore.QSize(300, 16777215))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB")
        font.setPointSize(9)
        self.label_A_2.setFont(font)
        self.label_A_2.setStyleSheet("background-color : rgb(255, 219, 135);\n"
"border-style : outset;\n"
"border-width : 2px;\n"
"border-radius : 10px;\n"
"border-color : gray;\n"
"min-height : 20px;\n"
"min-width : 20px;\n"
"color : black;\n"
"")
        self.label_A_2.setFrameShape(QtWidgets.QFrame.Box)
        self.label_A_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_A_2.setLineWidth(20)
        self.label_A_2.setMidLineWidth(0)
        self.label_A_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_A_2.setIndent(10)
        self.label_A_2.setObjectName("label_A_2")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)
        self.toolButton = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton.setGeometry(QtCore.QRect(335, 454, 42, 42))
        self.toolButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.toolButton.setStyleSheet("border-radius : 21px;\n"
"min-height : 20px;\n"
"min-width : 20px;\n"
"")
        self.toolButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("PycharmProjects/PROJECTS/Picture/75351-telegram-icons-computer-logo-free-clipart-hq.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton.setIcon(icon)
        self.toolButton.setIconSize(QtCore.QSize(40, 40))
        self.toolButton.setAutoExclusive(False)
        self.toolButton.setAutoRepeatDelay(0)
        self.toolButton.setAutoRepeatInterval(0)
        self.toolButton.setPopupMode(QtWidgets.QToolButton.InstantPopup)
        self.toolButton.setAutoRaise(True)
        self.toolButton.setObjectName("toolButton")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(44, 460, 281, 27))
        self.pushButton.setStyleSheet("border : none;")
        self.pushButton.setText("")
        self.pushButton.setFlat(True)
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.pushButton.clicked.connect(self.test)

    def test(self):
        print("HASHSH")

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Bacotan"))
        self.label_A.setText(_translate("MainWindow", "Chat From A"))
        self.label_A_2.setText(_translate("MainWindow", "Chat From B"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
