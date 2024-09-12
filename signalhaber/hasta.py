from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSignal
from hastabilgi import Ui_widget_hastaekrani

class HastaPage(QWidget):
    hastasinyali=pyqtSignal(str)
    
    def __init__(self):
        super().__init__()
        self.HastaFormu=Ui_widget_hastaekrani()
        self.HastaFormu.setupUi(self)
        self.HastaFormu.pushButton_hastagonder.clicked.connect(self.HastaMesaj)
        
    def HastaMesaj(self):
        bilgi=self.HastaFormu.textEdit_hastamesaj.toPlainText()
        self.hastasinyali.emit(bilgi)