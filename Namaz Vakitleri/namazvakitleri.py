from PyQt5 import QtCore, QtGui, QtWidgets
import namazsaatleri,sehir_url,url

sehir_id=0
ilce_id=0


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(681, 511)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(0, 0, 681, 511))
        self.label_9.setObjectName("label_3")
        self.label_9.setPixmap(QtGui.QPixmap("resim.jpg"))
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(40, 20, 461, 61))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(10, 0, 10, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.comboBox = QtWidgets.QComboBox(self.horizontalLayoutWidget)
        self.comboBox.setObjectName("comboBox")

        for i in sehir_url.sehir_url_cagirma():
            self.comboBox.addItem(i["SehirAdi"])

        self.horizontalLayout.addWidget(self.comboBox)

        self.comboBox.activated.connect(self.handleActivated)

        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(40, 110, 461, 61))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(10, 0, 10, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.comboBox_2 = QtWidgets.QComboBox(self.horizontalLayoutWidget_3)
        self.comboBox_2.setObjectName("comboBox_2")
        self.horizontalLayout_3.addWidget(self.comboBox_2)

        self.comboBox_2.activated.connect(self.handleActivated1)

        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(39, 280, 461, 241))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.label_6 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)
        self.label_7 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.verticalLayout.addWidget(self.label_7)
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.label_8 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.verticalLayout.addWidget(self.label_8)
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(40, 200, 461, 61))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(10, 0, 10, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_9 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_2.addWidget(self.label_9)
        self.comboBox_3 = QtWidgets.QComboBox(self.horizontalLayoutWidget_2)
        self.comboBox_3.setObjectName("comboBox_3")
        self.horizontalLayout_2.addWidget(self.comboBox_3)
        self.comboBox_3.activated.connect(self.handleActivated2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setStyleSheet('color: yellow')
        self.label.setFont(QtGui.QFont("Times", 13))
        self.label.setText(_translate("MainWindow", "Şehir Seçiniz"))
        self.label_2.setStyleSheet('color: yellow')
        self.label_2.setFont(QtGui.QFont("Times", 13))
        self.label_2.setText(_translate("MainWindow", "İlçe Seçiniz"))
        self.label_9.setStyleSheet('color: yellow')
        self.label_9.setFont(QtGui.QFont("Times", 13))
        self.label_9.setText(_translate("MainWindow", "Tarih Seçiniz"))

    def handleActivated(self,index):
        self.comboBox_2.clear()
        for i in sehir_url.sehir_url_cagirma():
            if self.comboBox.itemText(index) == i["SehirAdi"]:
                global sehir_id
                sehir_id = i["SehirID"]
        for i in url.ilce_url_cagirma(sehir_id):
            self.comboBox_2.addItem(i["IlceAdi"])

    def handleActivated1(self, index):
        self.comboBox_3.clear()
        for i in url.ilce_url_cagirma(sehir_id):
            if self.comboBox_2.itemText(index) == i["IlceAdi"]:
                global ilce_id
                ilce_id=(i["IlceID"])
        for i in namazsaatleri.namaz_vakitleri(ilce_id):
            self.comboBox_3.addItem(str(i["MiladiTarihUzun"]))

    def handleActivated2(self, index):
        self.label_4.clear()
        self.label_6.clear()
        self.label_7.clear()
        self.label_5.clear()
        self.label_8.clear()
        self.label_3.clear()
        for i in namazsaatleri.namaz_vakitleri(ilce_id):
            if self.comboBox_3.itemText(index) == str(i["MiladiTarihUzun"]):
                self.label_4.setText("İmsak Vakti : {}".format(i["Imsak"]))
                self.label_4.setStyleSheet('color: yellow')
                self.label_4.setFont(QtGui.QFont("Times", 13))
                self.label_6.setText("Güneş Vakti : {}".format(i["Gunes"]))
                self.label_6.setStyleSheet('color: yellow')
                self.label_6.setFont(QtGui.QFont("Times", 13))
                self.label_7.setText("Öğle Vakti : {}".format(i["Ogle"]))
                self.label_7.setStyleSheet('color: yellow')
                self.label_7.setFont(QtGui.QFont("Times", 13))
                self.label_5.setText("İkindi Vakti : {}".format(i["Ikindi"]))
                self.label_5.setStyleSheet('color: yellow')
                self.label_5.setFont(QtGui.QFont("Times", 13))
                self.label_8.setText("Akşam Vakti : {}".format(i["Aksam"]))
                self.label_8.setStyleSheet('color: yellow')
                self.label_8.setFont(QtGui.QFont("Times", 13))
                self.label_3.setText("Yatsı Vakti : {}".format(i["Yatsi"]))
                self.label_3.setStyleSheet('color: yellow')
                self.label_3.setFont(QtGui.QFont("Times", 13))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

