from PyQt5 import QtCore, QtGui, QtWidgets
from Start import *
import socket, sys, time
class RoomChatting(object):
    def __init__(self) :
        self.user_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_address = (('localhost', 8080))
        self.user_socket.connect(self.server_address)

        self.MainWindow = QtWidgets.QMainWindow()
        Start(self, self.MainWindow)
        self.Button_Next.clicked.connect(self.goto_setupUI)
        self.MainWindow.show()

    def goto_setupUI(self):
        self.setupUi(self.MainWindow, 'P')

    def setupUi(self, MainWindow, info):
        MainWindow.resize(400, 500)
        MainWindow.setMinimumSize(QtCore.QSize(400, 500))
        MainWindow.setMaximumSize(QtCore.QSize(400, 500))
        MainWindow.setWindowIcon(QtGui.QIcon("../Picture/Icon.png"))

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.background = QtWidgets.QLabel(self.centralwidget)
        self.background.setGeometry(QtCore.QRect(0, 0, 400, 500))
        self.background.setText("")
        self.background.setPixmap(QtGui.QPixmap("../Picture/Chatting_" + info + ".png"))
        self.background.setObjectName("background")

        self.RoomChat = QtWidgets.QScrollArea(self.centralwidget)
        self.RoomChat.setGeometry(QtCore.QRect(10, 60, 380, 370))
        self.RoomChat.setMinimumSize(QtCore.QSize(380, 370))
        self.RoomChat.setMaximumSize(QtCore.QSize(380, 16777215))
        self.RoomChat.setStyleSheet("background-color:transparent;")
        self.RoomChat.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.RoomChat.setFrameShadow(QtWidgets.QFrame.Raised)
        self.RoomChat.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.RoomChat.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.RoomChat.setWidgetResizable(False)
        self.RoomChat.setObjectName("RoomChat")
        self.HistoryChat = QtWidgets.QWidget()
        self.HistoryChat.setGeometry(QtCore.QRect(0, 0, 380, 370))
        self.HistoryChat.setObjectName("HistoryChat")
        self.RoomChat.setWidget(self.HistoryChat)

        self.labelChat = list()

        self.Button_Send = QtWidgets.QPushButton(self.centralwidget)
        self.Button_Send.setGeometry(QtCore.QRect(336, 455, 40, 40))
        self.Button_Send.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Button_Send.setStyleSheet("border : none;")
        self.Button_Send.setText("")
        self.Button_Send.setFlat(True)

        self.input_Pesan = QtWidgets.QLineEdit(self.centralwidget)
        self.input_Pesan.setGeometry(QtCore.QRect(40, 462, 284, 23))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHeightForWidth(self.input_Pesan.sizePolicy().hasHeightForWidth())
        self.input_Pesan.setSizePolicy(sizePolicy)
        self.input_Pesan.setMinimumSize(QtCore.QSize(284, 23))
        self.input_Pesan.setMaximumSize(QtCore.QSize(284, 50))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB")
        font.setPointSize(9)
        self.input_Pesan.setFont(font)
        self.input_Pesan.setMouseTracking(True)
        self.input_Pesan.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.input_Pesan.setAcceptDrops(True)
        self.input_Pesan.setMaxLength(500)
        self.input_Pesan.setFrame(False)
        self.input_Pesan.setObjectName("input_Pesan")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.Button_Send.clicked.connect(self.sendMessage)

        self.MainWindow.show()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Bacotan"))
        self.input_Pesan.setPlaceholderText(_translate("MainWindow", "Masukkan pesan"))

    def sendMessage(self):
        if len(self.input_Pesan.text()) == 0:
            self.receiveMessage()

        else:
            self.user_socket.sendall(self.input_Pesan.text().encode())

            height = 25
            width = self.input_Pesan.fontMetrics().boundingRect(
                self.input_Pesan.text()).width() + 25  # Get Lenght Pixel for lineEdit Text
            X = 340 - width

            if len(self.labelChat) == 0:
                Y = 20

            else:
                Y = self.labelChat[len(self.labelChat) - 1].y() + 35

            self.label_A = QtWidgets.QLabel(self.HistoryChat)
            self.label_A.setGeometry(QtCore.QRect(X, Y, width, height))
            self.label_A.setMinimumSize(QtCore.QSize(24, 24))
            self.label_A.setMaximumSize(QtCore.QSize(300, 16777215))
            font = QtGui.QFont()
            font.setFamily("Berlin Sans FB")
            font.setPointSize(9)
            self.label_A.setFont(font)
            self.label_A.setStyleSheet(
                "background-color : rgb(220, 139, 45);\nborder-style : outset;\nborder-width : 2px;\nborder-radius : 10px;\nborder-color : gray;\nmin-height : 20px;\nmin-width : 20px;\ncolor : white;\n")
            self.label_A.setIndent(10)

            _translate = QtCore.QCoreApplication.translate
            self.label_A.setText(_translate("MainWindow", self.input_Pesan.text()))

            self.labelChat.append(self.label_A)
            self.labelChat[len(self.labelChat) - 1].name = "label_A"

            self.labelChat[len(self.labelChat) - 1].show()
            self.input_Pesan.setText("")

    def receiveMessage(self):
        try:
            self.user_socket.setblocking(False)
            self.data = self.user_socket.recv(512)

        except socket.timeout:
            pass

        else:
            self.data = self.data.decode("utf-8")

            height = 30
            width = self.input_Pesan.fontMetrics().boundingRect(self.input_Pesan.text()).width() + 25  # Get Lenght Pixel for lineEdit Text
            X = 40

            if len(self.labelChat) == 0:
                Y = 20

            else:
                Y = self.labelChat[len(self.labelChat) - 1].y() + 35

            self.label_B = QtWidgets.QLabel(self.HistoryChat)
            self.label_B.setGeometry(QtCore.QRect(X, Y, width, height))
            self.label_B.setMinimumSize(QtCore.QSize(24, 24))
            self.label_B.setMaximumSize(QtCore.QSize(300, 16777215))
            font = QtGui.QFont()
            font.setFamily("Berlin Sans FB")
            font.setPointSize(9)
            self.label_B.setFont(font)
            self.label_B.setStyleSheet(
                "background-color : rgb(255, 219, 135);\nborder-style : outset;\nborder-width : 2px;\nborder-radius : 10px;\nborder-color : gray;\nmin-height : 20px;\nmin-width : 20px;\ncolor : black;\n")
            self.label_B.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
            self.label_B.setIndent(10)

            _translate = QtCore.QCoreApplication.translate
            self.label_B.setText(_translate("MainWindow", self.data))

            width = self.label_B.fontMetrics().boundingRect(self.label_B.text()).width() + 25  # Get Lenght Pixel for lineEdit Text

            self.label_B.setGeometry(QtCore.QRect(X, Y, width, height))

            self.labelChat.append(self.label_B)
            self.labelChat[len(self.labelChat) - 1].name = "label_B"

            self.labelChat[len(self.labelChat) - 1].show()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = RoomChatting()
    sys.exit(app.exec())
