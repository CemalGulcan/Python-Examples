from PyQt5 import QtCore, QtGui, QtWidgets
import dovizbirimleri

a=0;b=0;c=0;d=0
class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(500, 439)
        self.label_9 = QtWidgets.QLabel(Form)
        self.label_9.setGeometry(QtCore.QRect(0, 0, 500, 439))
        self.label_9.setObjectName("label_3")
        self.label_9.setPixmap(QtGui.QPixmap("resim.jpg"))
        self.horizontalLayoutWidget = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 10, 361, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label.setMaximumSize(QtCore.QSize(900, 25))
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.comboBox = QtWidgets.QComboBox(self.horizontalLayoutWidget)
        self.comboBox.setMaximumSize(QtCore.QSize(75, 25))
        self.comboBox.setObjectName("comboBox")

        for i in dovizbirimleri.doviz_verileri():
            self.comboBox.addItem(i)
        self.horizontalLayout.addWidget(self.comboBox)

        self.comboBox.activated.connect(self.tikla)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(20, 70, 361, 41))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_2.setMaximumSize(QtCore.QSize(500, 25))
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.comboBox_2 = QtWidgets.QComboBox(self.horizontalLayoutWidget_2)
        self.comboBox_2.setMaximumSize(QtCore.QSize(75, 25))
        self.comboBox_2.setObjectName("comboBox_2")
        for i in dovizbirimleri.doviz_verileri():
            self.comboBox_2.addItem(i)
        self.horizontalLayout_2.addWidget(self.comboBox_2)
        self.comboBox_2.activated.connect(self.tikla2)
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(20, 120, 361, 41))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.label_3.setMaximumSize(QtCore.QSize(500, 25))
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.lineEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget_3)
        self.lineEdit.setMaximumSize(QtCore.QSize(75, 25))
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_3.addWidget(self.lineEdit)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(190, 170, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.click)
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(30, 219, 351, 21))
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Bozduracağınız Döviz Birimi"))
        self.label.setStyleSheet('color : yellow')
        self.label.setFont(QtGui.QFont("Times", 13))
        self.label_2.setText(_translate("Form", "Hangi Döviz Birimine Dönüştürülecek"))
        self.label_2.setStyleSheet('color : yellow')
        self.label_2.setFont(QtGui.QFont("Times", 13))
        self.label_3.setText(_translate("Form", "Miktar"))
        self.label_3.setStyleSheet('color : yellow')
        self.label_3.setFont(QtGui.QFont("Times", 13))
        self.pushButton.setText(_translate("Form", "Tamam"))
        self.pushButton.setStyleSheet('color : black')
        self.pushButton.setFont(QtGui.QFont("Times", 13))

    def tikla(self,index):
        global a,c
        a=self.comboBox.itemText(index)
        c = dovizbirimleri.doviz_verileri1(a)

    def click(self):
        self.label_4.setStyleSheet('color : yellow')
        self.label_4.setFont(QtGui.QFont("Times", 18))
        self.label_4.setText( "{} {} = {} {}".format(self.lineEdit.text(),a,str(d/c*int(self.lineEdit.text())),b))


    def tikla2(self,index):
        global b,d
        b=self.comboBox_2.itemText(index)
        d=dovizbirimleri.doviz_verileri1(b)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
