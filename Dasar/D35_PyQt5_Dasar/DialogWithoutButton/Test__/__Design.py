from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *

class Ui_Dialog(QWidget):

    def setupUi(self, Dialog):

       #Dialog.setObjectName("Dialog")
        Dialog.resize(422, 300)
        self.labelInfo = QtWidgets.QLabel(Dialog)
        self.labelInfo.setGeometry(QtCore.QRect(30, 40, 111, 16))
       #self.labelInfo.setObjectName("labelInfo")
        self.inputName = QtWidgets.QLineEdit(Dialog)
        self.inputName.setGeometry(QtCore.QRect(150, 40, 191, 20))
       #self.inputName.setObjectName("inputName")
        self.outputName = QtWidgets.QLabel(Dialog)
        self.outputName.setGeometry(QtCore.QRect(100, 100, 231, 31))
       #self.outputName.setObjectName("outputName")
        self.outputName.setText("")
        font = QtGui.QFont()
        font.setFamily("Consolas")
        self.outputName.setFont(font)
        self.outputName.setAlignment(QtCore.Qt.AlignCenter)
        self.tombolKlik_OK = QtWidgets.QPushButton(Dialog)
        self.tombolKlik_OK.setGeometry(QtCore.QRect(350, 40, 31, 21))
       #self.tombolKlik_OK.setObjectName("tombolKlik_OK")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog User"))
        self.labelInfo.setText(_translate("Dialog", "Masukkan Nama Anda :"))
        self.tombolKlik_OK.setText(_translate("Dialog", "OK"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
