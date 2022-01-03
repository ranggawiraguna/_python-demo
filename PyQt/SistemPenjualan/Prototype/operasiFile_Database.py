from PyQt5 import QtCore, QtGui, QtWidgets
import xlwt

def insertDataPenjualan(self) :
    self.db["cursor"].execute("SELECT kode_barang,jumlah_barang FROM data_penjualan")
    data = self.db["cursor"].fetchall()

    dataInfo = "Tidak Ditemukan"
    for item in data:
        if self.ui.pageInputDataPenjualan["inputKode"].text() == item[0]:
            jumlah_dataPenjualan = item[1]
            dataInfo = "Ditemukan"

    try :
        if dataInfo == "Ditemukan":
            self.db["cursor"].execute("""UPDATE data_penjualan SET jumlah_barang = '%d' WHERE kode_barang = '%s'"""
                                      % ((jumlah_dataPenjualan + int(self.ui.pageInputDataPenjualan["inputJumlah"].text())),
                                         self.ui.pageInputDataPenjualan["inputKode"].text()))

            self.db["cursor"].execute("""UPDATE data_penjualan SET keterangan = '%s' WHERE kode_barang = '%s'"""
                                      % (self.ui.pageInputDataPenjualan["inputKeterangan"].text(),
                                         self.ui.pageInputDataPenjualan["inputKode"].text()))

        else :
            self.db["cursor"].execute("""INSERT INTO data_penjualan VALUES('%s', '%s', '%d', '%s')"""
                                       % (self.ui.pageInputDataPenjualan["inputKode"].text(),
                                          self.ui.pageInputDataPenjualan["inputNama"].text(),
                                          int(self.ui.pageInputDataPenjualan["inputJumlah"].text()),
                                          self.ui.pageInputDataPenjualan["inputKeterangan"].text()))

    except :
        self.ui.pageInputDataPenjualan["infoInput"].setText("Terdapat kesalahan dalam melakukan Input Data!")

    else :
        self.ui.pageInputDataPenjualan["infoInput"].setText("Data berhasil di input kedalam database!")
        self.ui.pageInputDataPenjualan["inputKode"].setText("")
        self.ui.pageInputDataPenjualan["inputNama"].setText("")
        self.ui.pageInputDataPenjualan["inputJumlah"].setText("")
        self.ui.pageInputDataPenjualan["inputKeterangan"].setText("")

    self.db["koneksi"].commit()

def deleteDataPenjualan(self) :
    try:
        data = self.ui.pageDeleteDataPenjualan["TabelData"].selectedItems()

    except Exception as e :
        print(e)
        self.ui.pageDeleteDataPenjualan["labelInfo"].setText("Pilih baris data yang ingin dihapus!")

    else:
        self.db["cursor"].execute("""DELETE FROM data_penjualan WHERE kode_barang = '%s' """ % (data[0].text()))
        tampilkanDataPenjualan_2(self)
        self.ui.pageDeleteDataPenjualan["labelInfo"].setText("Data berhasil dihapus")
        self.db["koneksi"].commit()

def tampilkanDataPenjualan(self) :
    self.db["cursor"].execute("SELECT * FROM data_penjualan")
    data = self.db["cursor"].fetchall()
    self.ui.pageLihatDataPenjualan["TabelData"].setRowCount(len(data))

    for x in range(len(data)):
        for y in range(4):
            self.ui.pageLihatDataPenjualan["TabelData"].setItem(x, y, QtWidgets.QTableWidgetItem(str(data[x][y])))


def tampilkanDataPenjualan_2(self) :
    self.db["cursor"].execute("SELECT * FROM data_penjualan")
    data = self.db["cursor"].fetchall()
    self.ui.pageDeleteDataPenjualan["TabelData"].setRowCount(len(data))

    for x in range(len(data)) :
        for y in range(4):
            self.ui.pageDeleteDataPenjualan["TabelData"].setItem(x, y, QtWidgets.QTableWidgetItem(str(data[x][y])))


def saveDataPenjualan(self) :
    self.db["cursor"].execute("SELECT * FROM data_penjualan")
    data = self.db["cursor"].fetchall()

    file = xlwt.Workbook()

    sheet = file.add_sheet("Data Penjualan")
    sheet.write(0, 0, "Kode Barang")
    sheet.write(0, 1, "Nama Barang")
    sheet.write(0, 2, "Jumlah Barang")
    sheet.write(0, 3, "Keterangan")

    for row, item in zip(range(len(data)), data) :
        sheet.write(row+1, 0, item[0])
        sheet.write(row+1, 1, item[1])
        sheet.write(row+1, 2, item[2])
        sheet.write(row+1, 3, item[3])

    file.save(r"C:\Users\Rofiaa\Downloads\Data_Penjualan.xls")
    self.ui.pageLihatDataPenjualan["labelInfo"].setText('Data Berhasil Disimpan Pada "Downloads"')



#=================================================================================================================================================



def insertDataTerjual(self) :
    self.db["cursor"].execute("SELECT jumlah_barang FROM data_penjualan WHERE kode_barang = '%s'"
                              % (self.ui.pageInputDataTerjual["inputKode"].currentText()))
    jumlah_dataPenjualan = self.db["cursor"].fetchone()
    jumlah_dataPenjualan = int(jumlah_dataPenjualan[0])

    if int(self.ui.pageInputDataTerjual["inputJumlah"].text()) > jumlah_dataPenjualan:
        self.ui.pageInputDataTerjual["infoInput"].setText("Jumlah data terjual melebihi stok yang tersedia!")

    else :
        try :
            self.db["cursor"].execute("SELECT kode_barang,jumlah_barang FROM data_terjual")
            data = self.db["cursor"].fetchall()

            dataInfo = "Tidak Ditemukan"
            for item in data :
                if self.ui.pageInputDataTerjual["inputKode"].currentText() == item[0] :
                    jumlah_dataTerjual = item[1]
                    dataInfo = "Ditemukan"

            if dataInfo == "Ditemukan" :
                self.db["cursor"].execute("""UPDATE data_terjual SET jumlah_barang = '%d' WHERE kode_barang = '%s'"""
                                          % ((jumlah_dataTerjual + int(self.ui.pageInputDataTerjual["inputJumlah"].text())), self.ui.pageInputDataTerjual["inputKode"].currentText()))

                self.db["cursor"].execute("""UPDATE data_terjual SET keterangan = '%s' WHERE kode_barang = '%s'"""
                                          % (self.ui.pageInputDataTerjual["inputKeterangan"].text(), self.ui.pageInputDataTerjual["inputKode"].currentText()))

            else :
                self.db["cursor"].execute("""INSERT INTO data_terjual VALUES('%s', '%s', '%d', '%s')"""
                                           % (self.ui.pageInputDataTerjual["inputKode"].currentText(),
                                              self.ui.pageInputDataTerjual["inputNama"].text(),
                                              int(self.ui.pageInputDataTerjual["inputJumlah"].text()),
                                              self.ui.pageInputDataTerjual["inputKeterangan"].text()))

                self.db["cursor"].execute("""UPDATE data_penjualan SET jumlah_barang = '%d' WHERE kode_barang = '%s'"""
                                          % ((jumlah_dataPenjualan - int(self.ui.pageInputDataTerjual["inputJumlah"].text())), self.ui.pageInputDataTerjual["inputKode"].currentText()))

        except Exception as e:
            self.ui.pageInputDataTerjual["infoInput"].setText("Terdapat kesalahan dalam melakukan Input Data!")
            print(e)

        else :
            self.ui.pageInputDataTerjual["infoInput"].setText("Data berhasil di input kedalam database!")
            self.ui.pageInputDataTerjual["inputKode"].setCurrentIndex(0)
            self.ui.pageInputDataTerjual["inputNama"].setText("")
            self.ui.pageInputDataTerjual["inputJumlah"].setText("")
            self.ui.pageInputDataTerjual["inputKeterangan"].setText("")

        self.db["koneksi"].commit()

def deleteDataTerjual(self) :
    try:
        data = self.ui.pageDeleteDataTerjual["TabelData"].selectedItems()

    except:
        self.ui.pageDeleteDataTerjual["labelInfo"].setText("Pilih baris data yang ingin dihapus!")

    else:
        self.db["cursor"].execute("""DELETE FROM data_terjual WHERE kode_barang = '%s' """ % (data[0].text()) )
        tampilkanDataTerjual_2(self)
        self.ui.pageDeleteDataTerjual["labelInfo"].setText("Data berhasil dihapus")
        self.db["koneksi"].commit()

def tampilkanDataTerjual(self) :
    self.db["cursor"].execute("SELECT * FROM data_terjual")
    data = self.db["cursor"].fetchall()
    self.ui.pageLihatDataTerjual["TabelData"].setRowCount(len(data))

    for x in range(len(data)):
        for y in range(4):
            self.ui.pageLihatDataTerjual["TabelData"].setItem(x, y, QtWidgets.QTableWidgetItem(str(data[x][y])))

def tampilkanDataTerjual_2(self) :
    self.db["cursor"].execute("SELECT * FROM data_terjual")
    data = self.db["cursor"].fetchall()
    self.ui.pageDeleteDataTerjual["TabelData"].setRowCount(len(data))

    for x in range(len(data)):
        for y in range(4):
            self.ui.pageDeleteDataTerjual["TabelData"].setItem(x, y, QtWidgets.QTableWidgetItem(str(data[x][y])))

def saveDataTerjual(self) :
    self.db["cursor"].execute("SELECT * FROM data_terjual")
    data = self.db["cursor"].fetchall()

    file = xlwt.Workbook()

    sheet = file.add_sheet("Data Terjual")
    sheet.write(0, 0, "Kode Barang")
    sheet.write(0, 1, "Nama Barang")
    sheet.write(0, 2, "Jumlah Barang")
    sheet.write(0, 3, "Keterangan")

    for row, item in zip(range(len(data)), data) :
        sheet.write(row+1, 0, item[0])
        sheet.write(row+1, 1, item[1])
        sheet.write(row+1, 2, item[2])
        sheet.write(row+1, 3, item[3])

    file.save(r"C:\Users\Rofiaa\Downloads\Data_Terjual.xls")
    self.ui.pageLihatDataTerjual["labelInfo"].setText('Data Berhasil Disimpan Pada "Downloads"')