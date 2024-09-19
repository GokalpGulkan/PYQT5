from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from donusumler.anasayfaUİ import *
from donusumler.hakkındaUİ import *
from PyQt5.QtCore import pyqtSlot
import sys



#UYGULAMA OLUŞTURMA 

uygulama=QApplication(sys.argv)
pencere_anasayfa=QMainWindow()
ui=Ui_MainWindow()
ui.setupUi(pencere_anasayfa)
pencere_anasayfa.show()

pencere_hakkinda=QDialog()
ui2=Ui_Dialog()
ui2.setupUi(pencere_hakkinda)


#VERİTABANI OLUŞTURMA

import sqlite3
global curs
global conn

conn=sqlite3.connect('veritabani.db')
curs=conn.cursor()
sorguCreTblSpor=("CREATE TABLE IF NOT EXISTS spor(                 \
                 Id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,    \
                 TCNo TEXT NOT NULL UNIQUE,                        \
                 SporcuAdi TEXT NOT NULL,                          \
                 SporcuSoyadi TEXT NOT NULL,                       \
                 KulupAdi TEXT NOT NULL,                           \
                 Brans TEXT NOT NULL,                              \
                 Cinsiyet TEXT NOT NULL,                           \
                 DTarihi TEXT NOT NULL,                            \
                 MHal TEXT NOT NULL,                               \
                 Kilo TEXT NOT NULL)")
curs.execute(sorguCreTblSpor)
conn.commit()
#KAYDET
def EKLE():
    _lineEdit_TCK=ui.lineEdit_TCK.text()
    _lineedit_Sporucadi=ui.lineEdit_Sporcuadi.text()
    _lineedit_SporcuSoyadi=ui.lineEdit_Sporcusoyadi.text()
    _comboBox_Sporkulubu=ui.comboBox_Sporkulubu.currentText()
    _listWidget_Brans=ui.listWidget_Brans.currentItem().text()
    _comboBox_Sporcucinsiyeti=ui.comboBox_Sporcucinsiyeti.currentText()
    _calendarWidget_Dogumtarihi=ui.calendarWidget_Dogumtarihi.selectedDate().toString(QtCore.Qt.ISODate)
    if ui.checkBox_Evli.isChecked():
        _medeniHal="Evli"
    elif ui.checkBox_Bekar.isChecked():
        _medeniHal="Bekar"
    _spinBox_Sporcukilosu=ui.spinBox_Sporcukilosu.value()
    
    
    curs.execute("INSERT INTO spor \
                     (TCNo,SporcuAdi,SporcuSoyadi,KulupAdi,Brans,Cinsiyet,DTarihi,MHal,Kilo) \
                      VALUES (?,?,?,?,?,?,?,?,?)", \
                            (_lineEdit_TCK, _lineedit_Sporucadi,_lineedit_SporcuSoyadi,_comboBox_Sporkulubu,_listWidget_Brans,_comboBox_Sporcucinsiyeti, \
                                _calendarWidget_Dogumtarihi,_medeniHal,_spinBox_Sporcukilosu))
    conn.commit()
    
    LISTELE()
#LİSTELE
def LISTELE():
    ui.tableWidget_Sporcubilgiler.clear()
    
    ui.tableWidget_Sporcubilgiler.setHorizontalHeaderLabels(('No','TC Kimlik No','Sporcu Adı','Sporcu Soyadı', \
                                                  'Kulüp Adı', 'Branş', 'Cinsiyet', 'Doğum Tarihi', \
                                                  'Medeni Hal', 'Sporcu Kilosu'))
    #tablodaki adları söyledik
    
    ui.tableWidget_Sporcubilgiler.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
    
    curs.execute("SELECT * FROM spor")
    
    for satirIndeks, satirVeri in enumerate(curs):
        for sutunIndeks, sutunVeri in enumerate (satirVeri):
            ui.tableWidget_Sporcubilgiler.setItem(satirIndeks,sutunIndeks,QTableWidgetItem(str(sutunVeri)))
    ui.lineEdit_TCK.clear()
    ui.lineEdit_Sporcusoyadi.clear()
    ui.lineEdit_Sporcuadi.clear()
    ui.comboBox_Sporkulubu.setCurrentIndex(-1)
    ui.spinBox_Sporcukilosu.setValue(55)
    
    curs.execute("SELECT COUNT(*) FROM spor")
    kayitSayisi=curs.fetchone()
    ui.label_Kayitsayisi.setText(str(kayitSayisi[0]))
    
    
LISTELE()

#ÇIKIŞ
def CIKIS():
    cevap=QMessageBox.question(pencere_anasayfa,"ÇIKIŞ","Programdan çıkmak istediğinize emin misiniz?",\
                        QMessageBox.Yes | QMessageBox.No )
    if cevap==QMessageBox.Yes:
        conn.close()
        sys.exit(uygulama.exec_())
    else:
        pencere_anasayfa.show()
        
#SİL
def SIL():
    cevap=QMessageBox.question(pencere_anasayfa,"KAYIT SİL","Kaydi silmek istediğinize emin misiniz?",\
        QMessageBox.Yes | QMessageBox.No )
    
    if cevap==QMessageBox.Yes:
        secili=ui.tableWidget_Sporcubilgiler.selectedItems()
        silinecek=secili[1].text()
        try:
            curs.execute("DELETE FROM spor WHERE TCNo='%s'" %(silinecek) )
            conn.commit()
            
            LISTELE()
            
            ui.statusbar.showMessage("KAYIT SİLME İŞLEMİ BAŞARIYLA GERÇEKLEŞTİ...",10000)
        except Exception as Hata:
                   ui.statusbar.showMessage("Şöyle bir hata ile karşılaşıldı:"+str(Hata))
    else:
        ui.statusbar.showMessage("Silme işlemi iptal edildi...",10000)
        
#ARAMA
def ARA():
    aranan1=ui.lineEdit_TCK.text()
    aranan2=ui.lineEdit_Sporcuadi.text()
    aranan3=ui.lineEdit_Sporcusoyadi.text()
    
    curs.execute("SELECT * FROM spor WHERE TCNo=? OR SporcuAdi=? OR SporcuSoyadi=? OR (SporcuAdi=? AND SporcuSoyadi=?)",  \
                 (aranan1,aranan2,aranan3,aranan2,aranan3))
    conn.commit()
    ui.tableWidget_Sporcubilgiler.clear()
    for satirIndeks,satirVeri in enumerate(curs):
        for sutunIndeks,sutunVeri in enumerate(satirVeri):
            ui.tableWidget_Sporcubilgiler.setItem(satirIndeks,sutunIndeks,QTableWidgetItem(str(sutunVeri)))
            
#DOLDUR

def DOLDUR():
    secili=ui.tableWidget_Sporcubilgiler.selectedItems()
    ui.lineEdit_TCK.setText(secili[1].text())
    ui.lineEdit_Sporcuadi.setText(secili[2].text())
    ui.lineEdit_Sporcusoyadi.setText(secili[3].text())
    ui.comboBox_Sporkulubu.setCurrentText(secili[4].text())
    if secili[5].text()=="Güreş":
        ui.listWidget_Brans.item(0).setSelected(True)
        ui.listWidget_Brans.setCurrentItem(ui.listWidget_Brans.item(0))
    if secili[5].text()=="Boks":
        ui.listWidget_Brans.item(1).setSelected(True)
        ui.listWidget_Brans.setCurrentItem(ui.listWidget_Brans.item(1))
    if secili[5].text()=="Karete":
        ui.listWidget_Brans.item(2).setSelected(True)
        ui.listWidget_Brans.setCurrentItem(ui.listWidget_Brans.item(2))
    if secili[5].text()=="Tekvando":
        ui.listWidget_Brans.item(3).setSelected(True)
        ui.listWidget_Brans.setCurrentItem(ui.listWidget_Brans.item(3))
    if secili[5].text()=="Aikido":
        ui.listWidget_Brans.item(4).setSelected(True)
        ui.listWidget_Brans.setCurrentItem(ui.listWidget_Brans.item(4))
        
    ui.comboBox_Sporcucinsiyeti.setCurrentText(secili[6].text())
    
    yil=int(secili[7].text()[0:4])
    ay=int(secili[7].text()[5:7])
    gun=int(secili[7].text()[8:10])
    
    ui.calendarWidget_Dogumtarihi.setSelectedDate(QtCore.QDate(yil,ay,gun))
    
    if secili[8].text=="Evli":
        ui.checkBox_Evli.setChecked(True)
    if secili[8].text=="Bekar":
        ui.checkBox_Bekar.setChecked(True)
        
    ui.spinBox_Sporcukilosu.setValue(int(secili[9].text()))


def GUNCELLE():
    
   cevap=QMessageBox.question(pencere_anasayfa,"KAYIT GÜNCELLE","Kaydı güncellemek istediğinize emin misiniz?",\
                         QMessageBox.Yes | QMessageBox.No)
   
   if cevap==QMessageBox.Yes:
        try:
            secili=ui.tableWidget_Sporcubilgiler.selectedItems()
            _Id=int(secili[0].text())
            _lineEdit_TCK=ui.lineEdit_TCK.text()
            _lineedit_Sporucadi=ui.lineEdit_Sporcuadi.text()
            _lineedit_SporcuSoyadi=ui.lineEdit_Sporcusoyadi.text()
            _comboBox_Sporkulubu=ui.comboBox_Sporkulubu.currentText()
            _listWidget_Brans=ui.listWidget_Brans.currentItem().text()
            _comboBox_Sporcucinsiyeti=ui.comboBox_Sporcucinsiyeti.currentText()
            _calendarWidget_Dogumtarihi=ui.calendarWidget_Dogumtarihi.selectedDate().toString(QtCore.Qt.ISODate)
            
            if ui.checkBox_Evli.isChecked():
                _medeniHal="Evli"
            if ui.checkBox_Bekar.isChecked():
                _medeniHal="Bekar"
                
            _spinBox_Sporcukilosu=ui.spinBox_Sporcukilosu.value()
            
            curs.execute("UPDATE spor SET TCNo=?, SporcuAdi=?, SporcuSoyadi=?, Kilo=?,   \
                         KulupAdi=?, Brans=?, Cinsiyet=?, DTarihi=?, MHal=? WHERE Id=?", \
                         (_lineEdit_TCK,_lineedit_Sporucadi, _lineedit_SporcuSoyadi, _spinBox_Sporcukilosu,\
                           _comboBox_Sporkulubu,_listWidget_Brans, _comboBox_Sporcucinsiyeti, _calendarWidget_Dogumtarihi,_medeniHal,_Id))
            conn.commit()
            
            LISTELE()
            
        except Exception as Hata:
            ui.statusbar.showMessage("Şöyle bir hata meydana geldi"+str(Hata))
   else:
       ui.statusbar.showMessage("Güncelleme iptal edildi",1000)
       
def HAKKINDA():
    pencere_hakkinda.show()
        

  
    
    
#SİNYAL-SLOT
ui.pushButton_Kayitekle.clicked.connect(EKLE)
ui.pushButton_Kayitlistele.clicked.connect(LISTELE)
ui.pushButton_Cikis.clicked.connect(CIKIS)
ui.pushButton_Kayitsil.clicked.connect(SIL)
ui.pushButton_Kayitara.clicked.connect(ARA)
ui.tableWidget_Sporcubilgiler.itemSelectionChanged.connect(DOLDUR)
ui.pushButton_Guncelle.clicked.connect(GUNCELLE)
ui.menuhakkinda.triggered.connect(HAKKINDA)

    

sys.exit(uygulama.exec_())