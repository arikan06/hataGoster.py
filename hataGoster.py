#buttonReply = QMessageBox.question(self, 'PyQt5 message', "Do you like PyQt5?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
#hata.setStyleSheet("QLabel{min-width: 700px;}")
try:
    import sys
    import json
except Exception as e:
    print(e)
try:
    from PyQt5.QtCore import QSize
    from PyQt5 import QtWidgets, QtGui
    from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QMessageBox, QPushButton, QInputDialog, QLineEdit
except ModuleNotFoundError as e:
    print('PyQt5 modülü bulunamadı.')
    print('PyQt5 modülü kütüphaneye ekleniyor...')
    import pip
    pip.main(['install','PyQt5'])
    print('PyQt5 kütüphanenize eklendi.')

try:
    with open("ayarlar.json", "r") as f:
        ayarlarJson = json.load(f)
except FileNotFoundError:
    print('ayarlar.json bulunamadı, ayarlar.json yaratılıyor..')
    with open('ayarlar.json','w') as f:
        ayarlarYazdir = {
         "gorsel" : "mertfsmal.png"
        }
        json.dump(ayarlarYazdir, f)
        print("ayarlar.json yaratıldı")
        print('----------------------------------------------')
        pass
except Exception as e:
    print('json hatası')
    print(e)
    input()

def gorseliGoster():
    w = AnotherWindow()
    w.show()

def hataGoster():
    gorsel = ayarlarJson['gorsel']
    try:
        hataGosterIcerikVeriEsit = hataGosterIcerikVeri.text()
        hataGosterBaslikVeriEsit = hataGosterBaslikVeri.text()
        if hataGosterIcerikVeriEsit == ' ':
            hataGosterIcerikVeriEsit = '[boş]'
        if hataGosterBaslikVeriEsit == ' ':
            hataGosterBaslikVeriEsit = '[boş]'
        hata = QMessageBox()
        hata.setWindowTitle(hataGosterBaslikVeriEsit)
        hata.setText(hataGosterIcerikVeriEsit)
        hataGosterSimge = QMessageBox.Critical
        hata.setIcon(hataGosterSimge)
        hata.setStandardButtons(QMessageBox.Cancel)
        try:
            hata.setWindowIcon(QtGui.QIcon(gorsel))
        except Exception as e:
            pass
        hataGosterGoster = hata.exec_()
    except Exception as e:
        print(e)
        input()

def kritikSimge():
    hataGosterSimge = QMessageBox.Critical

def sistemBildiri():
    bildiri = QMessageBox()
    bildiri.setWindowTitle('hataGoster.py')
    bildiriKodu = 'İşlem başarıyla tamamlandı.'
    bildiri.setText(bildiriKodu)
    bildiri.setIcon(QMessageBox.Information)
    bildiri.setStandardButtons(QMessageBox.Ok)
    bildiri.setWindowIcon(QtGui.QIcon('mertfsmal.png'))
    bildiriGoster = bildiri.exec_()

def gorseliKaldir():
    with open('ayarlar.json','w') as f:
        ayarlarYazdir = {
         "gorsel" : ""
        }
        json.dump(ayarlarYazdir, f)
        sistemBildiri()
def gorseliDegistir():
    yeniGorsel, ok = QInputDialog.getText(pencere, 'Görseli değiştir', 'Görselin yolunu girin.')
    if ok:
        with open('ayarlar.json','w') as f:
            ayarlarYazdir = {
             "gorsel" : yeniGorsel
            }
            json.dump(ayarlarYazdir, f)
            sistemBildiri()
uygulama = QApplication(sys.argv)
pencere = QMainWindow()
pencere.setWindowIcon(QtGui.QIcon('mertfsmal.png'))
pencere.setGeometry(200,200,300,300)
pencere.setMinimumSize(QSize(700,400))
pencere.setWindowTitle("hataGoster.py")

hataGosterBaslikVeri = QLineEdit(pencere)
hataGosterBaslikVeri.move(20, 40)
hataGosterBaslikVeri.setPlaceholderText('Gösterilecek başlığı giriniz.')
hataGosterBaslikVeri.resize(180,30)

hataGosterIcerikVeri = QLineEdit(pencere)
hataGosterIcerikVeri.move(20, 80)
hataGosterIcerikVeri.setPlaceholderText('Gösterilecek hatayı giriniz.')
hataGosterIcerikVeri.resize(180,30)

hataGosterTus = QPushButton(pencere)
hataGosterTus.setText('Hatayı göster')
hataGosterTus.clicked.connect(hataGoster)
hataGosterTus.resize(180,30)
hataGosterTus.move(20, 120)

gorselGosterTus = QPushButton(pencere)
gorselGosterTus.setText('Görseli göster')
gorselGosterTus.clicked.connect(gorseliGoster)
gorselGosterTus.resize(180,30)
gorselGosterTus.move(20,240)

gorselTus = QPushButton(pencere)
gorselTus.setText('Görseli değiştir')
gorselTus.clicked.connect(gorseliDegistir)
gorselTus.resize(180,30)
gorselTus.move(20,280)

gorselKaldirTus = QPushButton(pencere)
gorselKaldirTus.setText('Görseli kaldır')
gorselKaldirTus.clicked.connect(gorseliKaldir)
gorselKaldirTus.resize(180,30)
gorselKaldirTus.move(20,320)


simgeTus = QPushButton(pencere)
simgeTus.setText('Soru simgesi')
simgeTus.clicked.connect(gorseliGoster)
simgeTus.resize(180,30)
simgeTus.move(220,80)

simgeTus = QPushButton(pencere)
simgeTus.setText('Bilgilendirme Simgesi')
simgeTus.clicked.connect(gorseliGoster)
simgeTus.resize(180,30)
simgeTus.move(220,120)

simgeTus = QPushButton(pencere)
simgeTus.setText('Uyarı Simgesi')
simgeTus.clicked.connect(gorseliGoster)
simgeTus.resize(180,30)
simgeTus.move(220,160)

simgeTus = QPushButton(pencere)
simgeTus.setText('Kritik simgesi')
simgeTus.clicked.connect(kritikSimge)
simgeTus.resize(180,30)
simgeTus.move(220,200)

gorselIcerik = QLabel(pencere)
gorselIcerik.setText(ayarlarJson['gorsel'])
gorselIcerik.move(20, 200)

pencere.show()
sys.exit(uygulama.exec_())
