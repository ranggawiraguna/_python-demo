from PyQt5 import QtCore, QtGui, QtWidgets


def Start(self, MainWindow):
    MainWindow.setObjectName("MainWindow")
    MainWindow.resize(400, 500)
    MainWindow.setMinimumSize(QtCore.QSize(400, 500))
    MainWindow.setMaximumSize(QtCore.QSize(400, 500))
    self.centralwidget = QtWidgets.QWidget(MainWindow)
    self.centralwidget.setObjectName("centralwidget")
    self.Button_Next = QtWidgets.QPushButton(self.centralwidget)
    self.Button_Next.setGeometry(QtCore.QRect(110, 160, 160, 160))
    self.Button_Next.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
    self.Button_Next.setStyleSheet("border : none;")
    self.Button_Next.setText("")
    icon = QtGui.QIcon()
    icon.addPixmap(QtGui.QPixmap("../Picture/Icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    self.Button_Next.setIcon(icon)
    self.Button_Next.setIconSize(QtCore.QSize(160, 160))
    self.Button_Next.setFlat(True)
    self.Button_Next.setObjectName("Button_Send")
    self.label = QtWidgets.QLabel(self.centralwidget)
    self.label.setGeometry(QtCore.QRect(70, 320, 241, 41))
    font = QtGui.QFont()
    font.setFamily("Kristen ITC")
    font.setPointSize(12)
    font.setBold(True)
    font.setUnderline(True)
    font.setWeight(75)
    self.label.setFont(font)
    self.label.setAlignment(QtCore.Qt.AlignCenter)
    self.label.setObjectName("label")
    MainWindow.setCentralWidget(self.centralwidget)

    QtCore.QMetaObject.connectSlotsByName(MainWindow)

    _translate = QtCore.QCoreApplication.translate
    MainWindow.setWindowTitle(_translate("MainWindow", "Bacotan"))
    self.label.setText(_translate("MainWindow", "Press Icon For Chatting!"))


