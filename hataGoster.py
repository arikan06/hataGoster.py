try:
    import sys
    import json
except Exception as e:
    print(e)
try:
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
         "gorsel" : "hataGoster.png"
        }
        json.dump(ayarlarYazdir, f)
        print("ayarlar.json yaratıldı")
        print('----------------------------------------------')
        pass
except Exception as e:
    print(e)
    input('')

gorsel = ayarlarJson['gorsel']

def hataGoster():
    try:
        hata = QMessageBox()
        hata.setWindowTitle('Hata!')
        hata.setText('Hata!')
        hata.setIcon(QMessageBox.Critical)
        hata.setStandardButtons(QMessageBox.Cancel)
        hata.setWindowIcon(QtGui.QIcon(gorsel))
        hataGosterGoster = hata.exec_()
    except Exception as e:
        print(e)
        input()

def gorseliDegistir():
    text, ok = QInputDialog.getText('Input Dialog',
    'Enter your name:')
    if ok:
        print(text)
uygulama = QApplication(sys.argv)
pencere = QMainWindow()
pencere.setWindowIcon(QtGui.QIcon(gorsel))
pencere.setGeometry(200,200,300,300)
pencere.setWindowTitle("hataGoster.py")

hataGosterVeri = QLineEdit(pencere)
hataGosterVeri.move(20, 40)
hataGosterVeri.setPlaceholderText('Gösterilecek hatayı giriniz.')
hataGosterVeri.resize(200, 30)

hataGosterTus = QPushButton(pencere)
hataGosterTus.setText('Hatayı göster')
hataGosterTus.clicked.connect(hataGoster)
hataGosterTus.resize(180,30)
hataGosterTus.move(20, 80)

gorselTus = QPushButton(pencere)
gorselTus.setText('Görseli değiştir')
gorselTus.clicked.connect(gorseliDegistir)
gorselTus.resize(180,30)
gorselTus.move(20,140)

simgeTus = QPushButton(pencere)
simgeTus.setText('Simge')
simgeTus.clicked.connect(gorseliDegistir)
simgeTus.resize(180,30)
simgeTus.move(20,180)

simgeIcerik = QLabel(pencere)
simgeIcerik.setText(ayarlarJson['gorsel'])
simgeIcerik.move(210, 140)

pencere.show()
sys.exit(uygulama.exec_())
