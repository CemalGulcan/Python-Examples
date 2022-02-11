from PyQt5 import QtCore, QtGui, QtWidgets
import requests
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(450, 450)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(0, 0, 450, 450))
        self.label_3.setObjectName("label_3")
        self.label_3.setPixmap(QtGui.QPixmap("resim.jpg"))
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(300, 20, 141, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItems([
    "İSTANBUL", "ANKARA", "İZMİR", "ADANA", "ADIYAMAN", "AFYONKARAHİSAR", "AĞRI", "AKSARAY", "AMASYA",
    "ANTALYA", "ARDAHAN", "ARTVİN", "AYDIN", "BALIKESİR", "BARTIN", "BATMAN", "BAYBURT", "BİLECİK", "BİNGÖL",
    "BİTLİS", "BOLU", "BURDUR", "BURSA", "ÇANAKKALE", "ÇANKIRI", "ÇORUM", "DENİZLİ", "DİYARBAKIR", "DÜZCE", "EDİRNE",
    "ELAZIĞ", "ERZİNCAN", "ERZURUM", "ESKİŞEHİR", "GAZİANTEP", "GİRESUN", "GÜMÜŞHANE", "HAKKARİ", "HATAY", "IĞDIR",
    "ISPARTA", "KAHRAMANMARAŞ", "KARABÜK", "KARAMAN", "KARS", "KASTAMONU", "KAYSERİ", "KIRIKKALE", "KIRKLARELİ",
    "KIRŞEHİR", "KİLİS", "KOCAELİ", "KONYA", "KÜTAHYA", "MALATYA", "MANİSA", "MARDİN", "MERSİN", "MUĞLA", "MUŞ",
    "NEVŞEHİR", "NİĞDE", "ORDU", "OSMANİYE", "RİZE", "SAKARYA", "SAMSUN", "SİİRT", "SİNOP", "SİVAS", "ŞIRNAK",
    "TEKİRDAĞ", "TOKAT", "TRABZON", "TUNCELİ", "ŞANLIURFA", "UŞAK", "VAN", "YALOVA", "YOZGAT", "ZONGULDAK"])


        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(95, 20, 141, 16))
        self.label.setObjectName("label")
        self.label.setStyleSheet("font: 13pt Times")
        #self.label.setStyleSheet('color: green')
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 140, 400, 16))
        self.label_2.setObjectName("label_2")
        #self.label_2.setStyleSheet('color: yellow')
        self.label_2.setStyleSheet("font: 11pt Comic Sans MS")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 509, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Şehir Seçiniz"))
        self.label_2.setText(_translate("MainWindow", ""))
        self.comboBox.activated.connect(self.handleActivated)

    def handleActivated(self,index):
        self.label_2.clear()
        url="http://api.openweathermap.org/data/2.5/weather?appid=0c42f7f6b53b244c78a418f4f181282a&q="
        response = requests.get(url + str(self.comboBox.itemText(index)))
        veriler = response.json()
        #self.label_2.setText(self.comboBox.itemText(index))
        self.label_2.setText("{} Şehrinin Sıcaklığı ->> {} Derecedir.".format(self.comboBox.itemText(index),str(int(veriler["main"]["temp"]-273.15))))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
