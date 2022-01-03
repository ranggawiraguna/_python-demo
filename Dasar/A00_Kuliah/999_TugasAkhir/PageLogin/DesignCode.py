from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):

        MainWindow.resize(500, 500)
        MainWindow.setMinimumSize(QtCore.QSize(500, 500))
        MainWindow.setMaximumSize(QtCore.QSize(500, 500))
        iconWindow = QtGui.QIcon()
        iconWindow.addPixmap(QtGui.QPixmap("P_Icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(iconWindow)
        self.centralwidget = QtWidgets.QWidget(MainWindow)

        self.frameDesign = QtWidgets.QLabel(self.centralwidget)
        self.frameDesign.setGeometry(QtCore.QRect(0, 0, 500, 500))
        self.frameDesign.setMinimumSize(QtCore.QSize(500, 500))
        self.frameDesign.setMaximumSize(QtCore.QSize(500, 500))
        self.frameDesign.setText("")
        self.frameDesign.setPixmap(QtGui.QPixmap("P_FrameDesain.jpg"))
        self.frameDesign.setScaledContents(True)

        self.Shapes_ID = QtWidgets.QLabel(self.centralwidget)
        self.Shapes_ID.setGeometry(QtCore.QRect(150, 180, 199, 29))
        self.Shapes_ID.setText("")
        self.Shapes_ID.setPixmap(QtGui.QPixmap("P_ShapesID.png"))
        self.Shapes_ID.setScaledContents(True)

        self.Shapes_PASS = QtWidgets.QLabel(self.centralwidget)
        self.Shapes_PASS.setGeometry(QtCore.QRect(150, 220, 199, 29))
        self.Shapes_PASS.setText("")
        self.Shapes_PASS.setPixmap(QtGui.QPixmap("P_ShapesPWD.png"))
        self.Shapes_PASS.setScaledContents(True)

        self.buttonLogin = QtWidgets.QToolButton(self.centralwidget)
        self.buttonLogin.setGeometry(QtCore.QRect(210, 260, 81, 25))
        self.buttonLogin.setMinimumSize(QtCore.QSize(81, 25))
        self.buttonLogin.setMaximumSize(QtCore.QSize(81, 25))
        self.buttonLogin.setText("")
        iconButtonLogin = QtGui.QIcon()
        iconButtonLogin.addPixmap(QtGui.QPixmap("P_ButtonLogin.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonLogin.setIcon(iconButtonLogin)
        self.buttonLogin.setIconSize(QtCore.QSize(81, 25))
        self.buttonLogin.setAutoRaise(True)

        self.inputID = QtWidgets.QLineEdit(self.centralwidget)
        self.inputID.setGeometry(QtCore.QRect(210, 184, 135, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.inputID.sizePolicy().hasHeightForWidth())
        self.inputID.setSizePolicy(sizePolicy)

        self.inputPASS = QtWidgets.QLineEdit(self.centralwidget)
        self.inputPASS.setGeometry(QtCore.QRect(210, 224, 135, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.inputPASS.sizePolicy().hasHeightForWidth())
        self.inputPASS.setSizePolicy(sizePolicy)
        self.inputPASS.setFrame(True)
        self.inputPASS.setEchoMode(QtWidgets.QLineEdit.Password)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Aplikasi COBAAN"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
