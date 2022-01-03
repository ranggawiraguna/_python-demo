from PyQt5.QtWidgets import QMainWindow, QApplication
from Prototype.MainWindow import *

class mainApplication(QMainWindow) :
    def __init__(self) :
        super().__init__()
        self.ui = Ui_MainWindow() #Mengambil Class untuk Dialog yang dibuat sebelumnya
        self.ui.setupUi(self, "pageLogin")

        self.ui.pageLogin["buttonLogin"].clicked.connect(self.eventLogin)

    def eventLogin(self) :

        dataListID = ["Rangga", "Fasya"]

        if self.ui.pageLogin["inputID"].text() not in dataListID :
            self.ui.pageLogin["Notice"].setText("ID/PASS yang dimasukkan salah!")

        else :
            del self.ui.pageLogin
            self.ui.setupUi(self, "pageBiodata")
            self.show()

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    MainWindow = mainApplication()
    MainWindow.show()
    sys.exit(app.exec_())
