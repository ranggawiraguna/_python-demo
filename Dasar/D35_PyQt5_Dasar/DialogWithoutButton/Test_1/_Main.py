from PyQt5.QtWidgets import QDialog, QApplication
from D35_PyQt5_Dasar.DialogWithoutButton.Test_1.__Design import *

class newFormatWIndow(QDialog) :
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog() #Mengambil Class untuk Dialog yang dibuat sebelumnya
        self.ui.setupUi(self)
        self.ui.tombolKlik_OK.clicked.connect(self.tampilkanPesan)
        self.show()

    def tampilkanPesan(self):
        self.ui.outputName.setText("Hallo " + self.ui.inputName.text())

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    mainWindow = newFormatWIndow()
    mainWindow.show()
    sys.exit(app.exec_())
