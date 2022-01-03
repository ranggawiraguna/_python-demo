from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):

    def setupUi(self, MainWindow) :
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(589, 411)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setGeometry(100, 100, 589, 411)
        Background = QtGui.QImage("Background.jpg")
        SizeBG = Background.scaled(QtCore.QSize(300,200))

        palette = QtGui.QPalette()
        palette.setBrush(QtGui.QPalette.Window, QtGui.QBrush(SizeBG))
        self.centralwidget.setPalette(palette)
        self.centralwidget.show()

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(0,0,589,411)

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(100, 90, 31, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(100, 120, 41, 16))
        self.label_2.setObjectName("label_2")
        self.judul = QtWidgets.QLabel(self.centralwidget)
        self.judul.setGeometry(QtCore.QRect(120, 30, 351, 51))
        font = QtGui.QFont()
        font.setFamily("Rage Italic")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.judul.setFont(font)
        self.judul.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.judul.setFrameShadow(QtWidgets.QFrame.Plain)
        self.judul.setAlignment(QtCore.Qt.AlignCenter)
        self.judul.setObjectName("judul")
        self.inputID = QtWidgets.QLineEdit(self.centralwidget)
        self.inputID.setGeometry(QtCore.QRect(150, 90, 301, 20))
        self.inputID.setObjectName("inputID")
        self.inputPASS = QtWidgets.QLineEdit(self.centralwidget)
        self.inputPASS.setGeometry(QtCore.QRect(150, 120, 301, 20))
        self.inputPASS.setObjectName("inputPASS")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(260, 160, 75, 23))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "AKADEMIK UHAMKA"))
        self.label.setText(_translate("MainWindow", "ID      :"))
        self.label_2.setText(_translate("MainWindow", "PASS :"))
        self.judul.setText(_translate("MainWindow", "AKADEMIK ONLINE"))
        self.pushButton.setText(_translate("MainWindow", "LOGIN"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
