import pymysql
import xlwt
from PyQt5.QtWidgets import QMainWindow, QApplication
from Prototype.mainWindow import *

class mainApplication(QMainWindow) :

    def __init__(self) :
        super().__init__()
        self.ui = Ui_MainWindow() #Mengambil Class untuk Dialog yang dibuat sebelumnya

        self.db = dict()
        self.db["koneksi"] = pymysql.connect("localhost", "root", "")
        self.db["cursor"] = self.db["koneksi"].cursor()
        self.db["cursor"].execute("SHOW DATABASES")
        listDB = self.db["cursor"].fetchall()
        self.status = str("Status")

        for database in listDB :
            if database[0] == 'db_penjualan_app' :
                self.status = "Login"
                self.db["cursor"].execute("USE db_penjualan_app")
                self.db["koneksi"].commit()
                self.ui.setupUi(self, "pageLogin")
                self.ui.pageLogin["buttonLogin"].clicked.connect(self.goto_pageManajemen)
                self.show()
                break

        else:
            self.status = "Daftar"
            self.ui.setupUi(self, "pageDaftar")
            self.ui.pageDaftar["buttonDaftar"].clicked.connect(self.goto_pageLogin)
            self.show()

    def verifikasiDaftar(self):
        if self.status == "Daftar" :
            if (self.ui.pageDaftar["inputPassword"].text()) == (self.ui.pageDaftar["inputRePassword"].text()):
                self.db["cursor"].execute("CREATE DATABASE db_penjualan_app")
                self.db["cursor"].execute("USE db_penjualan_app")
                self.db["cursor"].execute("CREATE TABLE data_akun(namaToko varchar(30), password varchar(30))")
                self.db["cursor"].execute("INSERT INTO data_akun VALUES ('%s', '%s')" %
                                          (self.ui.pageDaftar["inputNama"].text(),
                                           self.ui.pageDaftar["inputPassword"].text()))

                self.db["cursor"].execute("CREATE TABLE data_penjualan("
                                          "kode_barang VARCHAR(10) PRIMARY KEY,"
                                          "nama_barang VARCHAR(30) NOT NULL,"
                                          "jumlah_barang INT(10) NOT NULL,"
                                          "keterangan VARCHAR(30))")

                self.db["cursor"].execute("CREATE TABLE data_terjual("
                                          "kode_barang VARCHAR(10) PRIMARY KEY,"
                                          "nama_barang VARCHAR(30) NOT NULL,"
                                          "jumlah_barang INT(10) NOT NULL,"
                                          "keterangan VARCHAR(30),"
                                          "FOREIGN KEY(kode_barang) REFERENCES data_penjualan(kode_barang))")

                self.db["koneksi"].commit()
                self.status = "Daftar Sukses"

            else:
                self.ui.pageDaftar["notice"].setText("Pasword yang dimasukkan\ntidak sesuai")

    def goto_pageLogin(self) :
        self.verifikasiDaftar()

        if self.status == "Daftar Sukses" :
            clearWidget(self)
            self.ui.setupUi(self, "pageLogin")
            self.ui.pageLogin["buttonLogin"].clicked.connect(self.goto_pageManajemen)
            self.show()

    def verifikasiLogin(self):
        if self.status == "Daftar Sukses" or self.status == "Login":
            self.db["cursor"].execute("SELECT password FROM data_akun")
            key = self.db["cursor"].fetchone()

            if self.ui.pageLogin["inputKey"].text() in key:
                self.status = "Login Sukses"

            else:
                self.ui.pageLogin["notice"].setText("Key/Password yang dimasukkan salah!")
                self.status = "Login Gagal"

    def goto_pageManajemen(self) :
        self.verifikasiLogin()

        if self.status == "Login Sukses" :
            clearWidget(self)
            self.ui.setupUi(self, "pageManajemen")
            self.ui.pageManajemen["buttonPenjualan"].clicked.connect(self.goto_pageOperasiPenjualan)
            self.ui.pageManajemen["buttonTerjual"].clicked.connect(self.goto_pageOperasiTerjual)
            self.show()

    def goto_pageOperasiPenjualan(self) :
        clearWidget(self)
        self.ui.setupUi(self, "pageOperasiPenjualan")
        self.ui.pageOperasiPenjualan["buttonInput"].clicked.connect(self.goto_pageInputDataPenjualan)
        self.ui.pageOperasiPenjualan["buttonView"].clicked.connect(self.goto_pageLihatDataPenjualan)
        self.ui.pageOperasiPenjualan["buttonDelete"].clicked.connect(self.goto_pageDeleteDataPenjualan)
        self.ui.pageOperasiPenjualan["buttonBack"].clicked.connect(self.goto_pageManajemen)
        self.show()

    def goto_pageOperasiTerjual(self) :
        clearWidget(self)
        self.ui.setupUi(self, "pageOperasiTerjual")
        self.ui.pageOperasiTerjual["buttonInput"].clicked.connect(self.goto_pageInputDataTerjual)
        self.ui.pageOperasiTerjual["buttonView"].clicked.connect(self.goto_pageLihatDataTerjual)
        self.ui.pageOperasiTerjual["buttonDelete"].clicked.connect(self.goto_pageDeleteDataTerjual)
        self.ui.pageOperasiTerjual["buttonBack"].clicked.connect(self.goto_pageManajemen)
        self.show()

    def goto_pageInputDataPenjualan(self) :
        clearWidget(self)
        self.ui.setupUi(self, "pageInputDataPenjualan")
        self.ui.pageInputDataPenjualan["buttonBack"].clicked.connect(self.goto_pageOperasiPenjualan)
        self.ui.pageInputDataPenjualan["buttonInput"].clicked.connect(self.inputDataPenjualan)
        self.show()

    def inputDataPenjualan(self):
        if(" " in self.ui.pageInputDataPenjualan["inputKode"].text()) or (len(self.ui.pageInputDataPenjualan["inputKode"].text()) == 0) :
            self.ui.pageInputDataPenjualan["infoInput"].setText("Masukkan Data dengan benar!")

        else :
            insertDataPenjualan(self)

    def goto_pageInputDataTerjual(self) :
        clearWidget(self)
        self.ui.setupUi(self, "pageInputDataTerjual")

        self.db["cursor"].execute("SELECT kode_barang FROM data_penjualan")
        data = self.db["cursor"].fetchall()

        for key in data :
            self.ui.pageInputDataTerjual["inputKode"].addItem(str(key[0]))

        self.ui.pageInputDataTerjual["inputKode"].activated.connect(self.selectionData)
        self.ui.pageInputDataTerjual["buttonBack"].clicked.connect(self.goto_pageOperasiTerjual)
        self.ui.pageInputDataTerjual["buttonInput"].clicked.connect(self.inputDataTerjual)
        self.show()

    def selectionData(self):
        self.db["cursor"].execute("SELECT nama_barang FROM data_penjualan WHERE kode_barang = '%s'" % (self.ui.pageInputDataTerjual["inputKode"].currentText()))
        data = self.db["cursor"].fetchone()
        self.ui.pageInputDataTerjual["inputNama"].setText(str(data[0]))

    def inputDataTerjual(self) :
        if(" " in self.ui.pageInputDataTerjual["inputKode"].currentText()) or (len(self.ui.pageInputDataTerjual["inputKode"].currentText()) == 0) :
            self.ui.pageInputDataTerjual["infoInput"].setText("Masukkan Data dengan benar!")

        else :
            insertDataTerjual(self)

    def goto_pageLihatDataPenjualan(self) :
        clearWidget(self)
        self.ui.setupUi(self, "pageLihatDataPenjualan")
        tampilkanDataPenjualan(self)
        self.ui.pageLihatDataPenjualan["buttonBack"].clicked.connect(self.goto_pageOperasiPenjualan)
        self.ui.pageLihatDataPenjualan["buttonUnduh"].clicked.connect(self.eventUnduhP)
        self.show()

    def eventUnduhP(self):
        saveDataPenjualan(self)

    def goto_pageLihatDataTerjual(self) :
        clearWidget(self)
        self.ui.setupUi(self, "pageLihatDataTerjual")
        tampilkanDataTerjual(self)
        self.ui.pageLihatDataTerjual["buttonBack"].clicked.connect(self.goto_pageOperasiTerjual)
        self.ui.pageLihatDataTerjual["buttonUnduh"].clicked.connect(self.eventUnduhT)
        self.show()

    def eventUnduhT(self):
        saveDataTerjual(self)

    def goto_pageDeleteDataPenjualan(self) :
        clearWidget(self)
        self.ui.setupUi(self, "pageDeleteDataPenjualan")
        tampilkanDataPenjualan_2(self)
        self.ui.pageDeleteDataPenjualan["buttonBack"].clicked.connect(self.goto_pageOperasiPenjualan)
        self.ui.pageDeleteDataPenjualan["buttonDelete"].clicked.connect(self.eventDeleteDataPenjualan)
        self.show()

    def eventDeleteDataPenjualan(self):
        deleteDataPenjualan(self)

    def goto_pageDeleteDataTerjual(self) :
        clearWidget(self)
        self.ui.setupUi(self, "pageDeleteDataTerjual")
        tampilkanDataTerjual_2(self)
        self.ui.pageDeleteDataTerjual["buttonBack"].clicked.connect(self.goto_pageOperasiTerjual)
        self.ui.pageDeleteDataTerjual["buttonDelete"].clicked.connect(self.eventDeleteDataTerjual)
        self.show()

    def eventDeleteDataTerjual(self):
        deleteDataTerjual(self)


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    MainWindow = mainApplication()
    MainWindow.show()
    sys.exit(app.exec_())
