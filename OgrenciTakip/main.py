import sys
from PyQt5 import *
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget
from donusumler.ogrenciUİ import *
from PyQt5.QtWidgets import QTableWidgetItem
 
class Uygulama(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.ui.comboBox_Dogumyeri.addItems(["Adana", "Adıyaman", "Afyonkarahisar", "Ağrı", "Aksaray", "Amasya", "Ankara", "Antalya", "Ardahan", "Artvin", "Aydın", "Balıkesir", "Bartın", "Batman", "Bayburt", "Bilecik", "Bingöl", "Bitlis", "Bolu", "Burdur", "Bursa", "Çanakkale", "Çankırı", "Çorum", "Denizli", "Diyarbakır", "Düzce", "Edirne", "Elazığ", "Erzincan", "Erzurum", "Eskişehir", "Gaziantep", "Giresun", "Gümüşhane", "Hakkâri", "Hatay", "Iğdır", "Isparta", "İstanbul", "İzmir", "Kahramanmaraş", "Karabük", "Karaman", "Kars", "Kastamonu", "Kayseri", "Kilis", "Kırıkkale", "Kırklareli", "Kırşehir", "Kocaeli", "Konya", "Kütahya", "Malatya", "Manisa", "Mardin", "Mersin", "Muğla", "Muş", "Nevşehir", "Niğde", "Ordu", "Osmaniye", "Rize", "Sakarya", "Samsun", "Şanlıurfa", "Siirt", "Sinop", "Sivas", "Şırnak", "Tekirdağ", "Tokat", "Trabzon", "Tunceli", "Uşak", "Van", "Yalova", "Yozgat", "Zonguldak"])
        self.ui.pushButton_Kayitekle.clicked.connect(self.kayitekle)
        self.ui.pushButton_Kayitsil.clicked.connect(self.kayıtsil)
     
        
    def kayitekle(self):
        ad=self.ui.lineEdit_Ad.text()
        soyad=self.ui.lineEdit_Soyad.text()
        tc=self.ui.lineEdit_TCNo.text()
        
        cinsiyetgrup=self.ui.groupBox_Cinsiyet.findChildren(QtWidgets.QRadioButton)
        for i in cinsiyetgrup:
            if i.isChecked():
                cinsiyet=i.text()
        egitimgrup=self.ui.groupBox_Egitimturu.findChildren(QtWidgets.QRadioButton)
        for i in egitimgrup:
            if i.isChecked():
                egitimturu=i.text()
                
        dogumyeri=self.ui.comboBox_Dogumyeri.currentText()
        
        kayitders=self.ui.listWidget_Dersler.currentItem().text()
        
        dogumtarihi=self.ui.calendarWidget_Dogumtarihi.selectedDate().toString("dd-MM-yyyy")
        
        satırsayısı=self.ui.tableWidget_Bilgi.rowCount()-1
       
        self.ui.tableWidget_Bilgi.setItem(satırsayısı,0,QTableWidgetItem(ad))
        self.ui.tableWidget_Bilgi.setItem(satırsayısı,1,QTableWidgetItem(soyad))
        self.ui.tableWidget_Bilgi.setItem(satırsayısı,2,QTableWidgetItem(tc))
        self.ui.tableWidget_Bilgi.setItem(satırsayısı,3,QTableWidgetItem(cinsiyet))
        self.ui.tableWidget_Bilgi.setItem(satırsayısı,4,QTableWidgetItem(dogumyeri))
        self.ui.tableWidget_Bilgi.setItem(satırsayısı,5,QTableWidgetItem(dogumtarihi))
        self.ui.tableWidget_Bilgi.setItem(satırsayısı,6,QTableWidgetItem(kayitders))
        self.ui.tableWidget_Bilgi.setItem(satırsayısı,7,QTableWidgetItem(egitimturu))
        
        self.ui.tableWidget_Bilgi.insertRow(satırsayısı+1)
        
    def kayıtsil(self):
        secili=self.ui.tableWidget_Bilgi.currentRow()
        self.ui.tableWidget_Bilgi.removeRow(secili)
        
def app():
    app=QtWidgets.QApplication(sys.argv)
    win=Uygulama()
    win.show()
    sys.exit(app.exec_())
app()