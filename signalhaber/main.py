
from PyQt5.QtWidgets import *
from hasta import Ui_widget_hastaekrani
from doktorbilgi import Ui_widget_doktor
from hasta import HastaPage
from PyQt5.QtCore import pyqtSignal



class HastaneSistemi(QWidget):
    def __init__(self):
        super().__init__()
        self.doktor=Ui_widget_doktor()
        self.doktor.setupUi(self)
        self.hasta=HastaPage()
        self.hasta.show()
        self.hasta.hastasinyali.connect(self.HastaBilgi)
        self.doktor.pushButton_doktorgonder.clicked.connect(self.DoktorBilgi)
        
    def DoktorBilgi(self):
        doktorbilgi=self.doktor.textEdit_doktormesaj.toPlainText()
        self.hasta.HastaFormu.textEdit_hastamesaj.setText(doktorbilgi)
        
    def HastaBilgi(self,bilgi):
        self.doktor.textEdit_doktormesaj.setText(bilgi)
        
        
    
       
        


app=QApplication([])
pencere=HastaneSistemi()
pencere.show()
app.exec_()