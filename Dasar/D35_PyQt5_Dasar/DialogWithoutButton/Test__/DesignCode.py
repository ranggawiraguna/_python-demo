from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 500)
        MainWindow.setMinimumSize(QtCore.QSize(500, 500))
        MainWindow.setMaximumSize(QtCore.QSize(500, 500))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("E:/Rangga Wiraguna/500px/Design/kisspng-muhammadiyah-university-of-prof-dr-hamka-fakulta-content-5b20ea1d510d53.913244531528883741332.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.background = QtWidgets.QLabel(self.centralwidget)
        self.background.setGeometry(QtCore.QRect(0, 0, 1001, 501))
        self.background.setText("")
        self.background.setPixmap(QtGui.QPixmap("E:/Rangga Wiraguna/500px/Design/BackGrounf-A(500x500).jpg"))
        self.background.setObjectName("background")
        self.gridLogin = QtWidgets.QLabel(self.centralwidget)
        self.gridLogin.setGeometry(QtCore.QRect(10, 30, 461, 451))
        self.gridLogin.setText("")
        self.gridLogin.setPixmap(QtGui.QPixmap("E:/Rangga Wiraguna/500px/Design/GRID-LOGIN.png"))
        self.gridLogin.setObjectName("gridLogin")
        self.judul = QtWidgets.QLabel(self.centralwidget)
        self.judul.setGeometry(QtCore.QRect(170, 120, 171, 20))
        self.judul.setText("")
        self.judul.setPixmap(QtGui.QPixmap("E:/Rangga Wiraguna/500px/Design/aaa.png"))
        self.judul.setObjectName("judul")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(160, 160, 47, 13))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(160, 190, 47, 13))
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(200, 160, 151, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(200, 190, 151, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(230, 220, 75, 23))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "SISTEM INFORMASI"))
        self.label.setText(_translate("MainWindow", "ID      :"))
        self.label_2.setText(_translate("MainWindow", "PASS :"))
        self.pushButton.setText(_translate("MainWindow", "LOGIN"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    input()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())