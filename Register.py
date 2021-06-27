from PyQt5 import QtCore, QtGui, QtWidgets

class Register(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(740, 478)
        self.label = QtWidgets.QLabel(Form)
        self.label.setEnabled(True)
        self.label.setGeometry(QtCore.QRect(0, 0, 741, 481))
        self.label.setMinimumSize(QtCore.QSize(400, 200))
        self.label.setMaximumSize(QtCore.QSize(900, 500))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: qconicalgradient(cx:0, cy:0, angle:135, stop:0 rgba(255, 255, 0, 69), stop:0.375 rgba(255, 255, 0, 69), stop:0.423533 rgba(251, 255, 0, 145), stop:0.45 rgba(247, 255, 0, 208), stop:0.477581 rgba(255, 244, 71, 130), stop:0.518717 rgba(255, 218, 71, 130), stop:0.55 rgba(255, 255, 0, 255), stop:0.57754 rgba(255, 203, 0, 130), stop:0.625 rgba(255, 255, 0, 69), stop:1 rgba(255, 255, 0, 69));")
        self.label.setText("")
        self.label.setObjectName("label")
        self.note = QtWidgets.QLabel(Form)
        self.note.setGeometry(QtCore.QRect(60, 10, 680, 50))
        self.note.setMinimumSize(QtCore.QSize(680, 50))
        self.note.setMaximumSize(QtCore.QSize(750, 50))
        self.note.setBaseSize(QtCore.QSize(10, 10))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.note.setFont(font)
        self.note.setToolTip("")
        self.note.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.note.setAutoFillBackground(False)
        self.note.setStyleSheet("border: 1px solid  rgb(0, 0, 0);\n"
                                "font: 75 14pt \"MS Shell Dlg 2\";\n"
                                "background-color: rgb(202, 167, 255);\n"
                                "\n"
                                "border-radius:10%;\n"
                                "\n"
                                "background-color: rgb(156, 234, 255);")
        self.note.setLineWidth(10)
        self.note.setMidLineWidth(10)
        self.note.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.note.setObjectName("note")
        self.gridLayoutWidget = QtWidgets.QWidget(Form)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(60, 70, 681, 261))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(10, 10, 10, 10)
        self.gridLayout.setObjectName("gridLayout")
        self.electronicWallet2 = QtWidgets.QSpinBox(self.gridLayoutWidget)
        self.electronicWallet2.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.electronicWallet2.setFont(font)
        self.electronicWallet2.setMaximum(1000000000)
        self.electronicWallet2.setObjectName("electronicWallet2")
        self.gridLayout.addWidget(self.electronicWallet2, 3, 3, 1, 1)
        self.Password = QtWidgets.QLabel(self.gridLayoutWidget)
        self.Password.setMinimumSize(QtCore.QSize(0, 40))
        self.Password.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.Password.setFont(font)
        self.Password.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";\n"
                                "color: rgb(0, 0, 0);\n"
                                "border: 1px solid  rgb(0, 0, 0);\n"
                                "background-color: qconicalgradient(cx:0.5, cy:0.5, angle:0, stop:0 rgba(220, 225, 131, 255), stop:1 rgba(255, 255, 255, 255));")
        self.Password.setObjectName("Password")
        self.gridLayout.addWidget(self.Password, 2, 4, 1, 1)
        self.electronicWallet = QtWidgets.QLabel(self.gridLayoutWidget)
        self.electronicWallet.setMinimumSize(QtCore.QSize(0, 40))
        self.electronicWallet.setMaximumSize(QtCore.QSize(16777215, 40))
        self.electronicWallet.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";\n"
                                        "color: rgb(0, 0, 0);\n"
                                        "border: 1px solid  rgb(0, 0, 0);\n"
                                        "background-color: qconicalgradient(cx:0.5, cy:0.5, angle:0, stop:0 rgba(220, 225, 131, 255), stop:1 rgba(255, 255, 255, 255));")
        self.electronicWallet.setObjectName("electronicWallet")
        self.gridLayout.addWidget(self.electronicWallet, 3, 4, 1, 1)
        self.PhoneNumber = QtWidgets.QLabel(self.gridLayoutWidget)
        self.PhoneNumber.setMinimumSize(QtCore.QSize(140, 40))
        self.PhoneNumber.setMaximumSize(QtCore.QSize(100, 40))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.PhoneNumber.setFont(font)
        self.PhoneNumber.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";\n"
                                        "color: rgb(0, 0, 0);\n"
                                        "border: 1px solid  rgb(0, 0, 0);\n"
                                        "background-color: qconicalgradient(cx:0.5, cy:0.5, angle:0, stop:0 rgba(220, 225, 131, 255), stop:1 rgba(255, 255, 255, 255));")
        self.PhoneNumber.setAlignment(QtCore.Qt.AlignCenter)
        self.PhoneNumber.setObjectName("PhoneNumber")
        self.gridLayout.addWidget(self.PhoneNumber, 1, 4, 1, 1)
        self.mobileLine = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.mobileLine.setMinimumSize(QtCore.QSize(200, 40))
        self.mobileLine.setStyleSheet("font: 75 16pt \"MS Shell Dlg 2\";\n"
                                "color: rgb(0, 0, 0);")
        self.mobileLine.setMaxLength(11)
        self.mobileLine.setAlignment(QtCore.Qt.AlignCenter)
        self.mobileLine.setObjectName("mobileLine")
        self.gridLayout.addWidget(self.mobileLine, 2, 0, 1, 1)
        self.type = QtWidgets.QLabel(self.gridLayoutWidget)
        self.type.setMaximumSize(QtCore.QSize(16777215, 50))
        self.type.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";\n"
                                "color: rgb(0, 0, 0);\n"
                                "border: 1px solid  rgb(0, 0, 0);\n"
                                "background-color: qconicalgradient(cx:0.5, cy:0.5, angle:0, stop:0 rgba(220, 225, 131, 255), stop:1 rgba(255, 255, 255, 255));")
        self.type.setObjectName("type")
        self.gridLayout.addWidget(self.type, 3, 2, 1, 1)
        self.postalCode = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.postalCode.setFont(font)
        self.postalCode.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";\n"
                                        "color: rgb(0, 0, 0);\n"
                                        "border: 1px solid  rgb(0, 0, 0);\n"
                                        "background-color: qconicalgradient(cx:0.5, cy:0.5, angle:0, stop:0 rgba(220, 225, 131, 255), stop:1 rgba(255, 255, 255, 255));")
        self.postalCode.setAlignment(QtCore.Qt.AlignCenter)
        self.postalCode.setObjectName("postalCode")
        self.gridLayout.addWidget(self.postalCode, 1, 2, 1, 1)
        self.postalCodeLine = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.postalCodeLine.setMinimumSize(QtCore.QSize(0, 40))
        self.postalCodeLine.setMaximumSize(QtCore.QSize(16777215, 40))
        self.postalCodeLine.setStyleSheet("font: 75 16pt \"MS Shell Dlg 2\";\n"
                                          "color: rgb(0, 0, 0);")
        self.postalCodeLine.setMaxLength(10)
        self.postalCodeLine.setAlignment(QtCore.Qt.AlignCenter)
        self.postalCodeLine.setObjectName("postalCodeLine")
        self.gridLayout.addWidget(self.postalCodeLine, 1, 0, 1, 1)
        self.mobile = QtWidgets.QLabel(self.gridLayoutWidget)
        self.mobile.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";\n"
                                "color: rgb(0, 0, 0);\n"
                                "border: 1px solid  rgb(0, 0, 0);\n"
                                "background-color: qconicalgradient(cx:0.5, cy:0.5, angle:0, stop:0 rgba(220, 225, 131, 255), stop:1 rgba(255, 255, 255, 255));")
        self.mobile.setObjectName("mobile")
        self.gridLayout.addWidget(self.mobile, 2, 2, 1, 1)
        self.PasswordLine = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.PasswordLine.setMinimumSize(QtCore.QSize(0, 40))
        self.PasswordLine.setStyleSheet("font: 75 16pt \"MS Shell Dlg 2\";\n"
                                        "color: rgb(0, 0, 0);")
        self.PasswordLine.setMaxLength(8)
        self.PasswordLine.setEchoMode(QtWidgets.QLineEdit.Password)
        self.PasswordLine.setAlignment(QtCore.Qt.AlignCenter)
        self.PasswordLine.setObjectName("PasswordLine")
        self.gridLayout.addWidget(self.PasswordLine, 2, 3, 1, 1)
        self.Fristname = QtWidgets.QLabel(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Fristname.sizePolicy().hasHeightForWidth())
        self.Fristname.setSizePolicy(sizePolicy)
        self.Fristname.setMinimumSize(QtCore.QSize(140, 0))
        self.Fristname.setMaximumSize(QtCore.QSize(200, 16777215))
        self.Fristname.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";\n"
                                        "color: rgb(0, 0, 0);\n"
                                        "border: 1px solid  rgb(0, 0, 0);\n"
                                        "background-color: qconicalgradient(cx:0.5, cy:0.5, angle:0, stop:0 rgba(220, 225, 131, 255), stop:1 rgba(255, 255, 255, 255));")
        self.Fristname.setAlignment(QtCore.Qt.AlignCenter)
        self.Fristname.setObjectName("Fristname")
        self.gridLayout.addWidget(self.Fristname, 0, 4, 1, 1)
        self.PhoneNumberLine = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.PhoneNumberLine.setMinimumSize(QtCore.QSize(100, 40))
        self.PhoneNumberLine.setMaximumSize(QtCore.QSize(300, 40))
        self.PhoneNumberLine.setStyleSheet("font: 75 16pt \"MS Shell Dlg 2\";\n"
                                        "color: rgb(0, 0, 0);")
        self.PhoneNumberLine.setMaxLength(11)
        self.PhoneNumberLine.setAlignment(QtCore.Qt.AlignCenter)
        self.PhoneNumberLine.setObjectName("PhoneNumberLine")
        self.gridLayout.addWidget(self.PhoneNumberLine, 1, 3, 1, 1)
        self.LastNameLine = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.LastNameLine.setMinimumSize(QtCore.QSize(100, 0))
        self.LastNameLine.setMaximumSize(QtCore.QSize(284, 40))
        self.LastNameLine.setStyleSheet("font: 75 16pt \"MS Shell Dlg 2\";\n"
                                        "color: rgb(0, 0, 0);")
        self.LastNameLine.setAlignment(QtCore.Qt.AlignCenter)
        self.LastNameLine.setObjectName("LastNameLine")
        self.gridLayout.addWidget(self.LastNameLine, 0, 0, 1, 1)
        self.LastName = QtWidgets.QLabel(self.gridLayoutWidget)
        self.LastName.setMinimumSize(QtCore.QSize(140, 40))
        self.LastName.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.LastName.setFont(font)
        self.LastName.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";\n"
                                "color: rgb(0, 0, 0);\n"
                                "border: 1px solid  rgb(0, 0, 0);\n"
                                "background-color: qconicalgradient(cx:0.5, cy:0.5, angle:0, stop:0 rgba(220, 225, 131, 255), stop:1 rgba(255, 255, 255, 255));\n"
                                "font: 75 12pt \"MS Shell Dlg 2\";")
        self.LastName.setAlignment(QtCore.Qt.AlignCenter)
        self.LastName.setObjectName("LastName")
        self.gridLayout.addWidget(self.LastName, 0, 2, 1, 1)
        self.FristnameLine = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.FristnameLine.setMinimumSize(QtCore.QSize(80, 40))
        self.FristnameLine.setMaximumSize(QtCore.QSize(300, 50))
        self.FristnameLine.setStyleSheet("font: 75 16pt \"MS Shell Dlg 2\";\n"
                                        "color: rgb(0, 0, 0);")
        self.FristnameLine.setAlignment(QtCore.Qt.AlignCenter)
        self.FristnameLine.setObjectName("FristnameLine")
        self.gridLayout.addWidget(self.FristnameLine, 0, 3, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.seller = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.seller.setMaximumSize(QtCore.QSize(130, 50))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.seller.setFont(font)
        self.seller.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                "\n"
                                "border: 1px solid  rgb(7, 44, 255);")
        self.seller.setObjectName("seller")
        self.gridLayout_2.addWidget(self.seller, 2, 0, 1, 1)
        self.customer = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.customer.setMinimumSize(QtCore.QSize(0, 50))
        self.customer.setMaximumSize(QtCore.QSize(130, 50))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.customer.setFont(font)
        self.customer.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                        "\n"
                                        "border: 1px solid  rgb(7, 44, 255);")
        self.customer.setObjectName("customer")
        self.gridLayout_2.addWidget(self.customer, 2, 1, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_2, 3, 0, 1, 1)
        self.Register = QtWidgets.QPushButton(Form)
        self.Register.setGeometry(QtCore.QRect(10, 400, 80, 40))
        self.Register.setMinimumSize(QtCore.QSize(80, 40))
        self.Register.setMaximumSize(QtCore.QSize(150, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.Register.setFont(font)
        self.Register.setStyleSheet("background-color: qconicalgradient(cx:0.5, cy:0.5, angle:0, stop:0 rgba(85, 255, 255, 255), stop:1 rgba(255, 255, 255, 255));\n"
                                "\n"
                                "border-radius: 10%;\n"
                                "\n"
                                "border: 1px solid rgb(0, 0, 0);")
        self.Register.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("register.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Register.setIcon(icon)
        self.Register.setIconSize(QtCore.QSize(60, 60))
        self.Register.setObjectName("Register")
        self.Back = QtWidgets.QPushButton(Form)
        self.Back.setGeometry(QtCore.QRect(0, 10, 41, 41))
        self.Back.setStyleSheet("background-color: qconicalgradient(cx:0.5, cy:0.5, angle:0, stop:0 rgba(85, 255, 255, 255), stop:1 rgba(255, 255, 255, 255));\n"
                                "\n"
                                "border-radius: 10%;\n"
                                "\n"
                                "border: 1px solid rgb(0, 0, 0);\n"
                                "\n"
                                "font: 75 12pt \"MS Shell Dlg 2\";")
        self.Back.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Back.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Back.setIcon(icon1)
        self.Back.setIconSize(QtCore.QSize(30, 30))
        self.Back.setObjectName("Back")
        self.Rusalt = QtWidgets.QLabel(Form)
        self.Rusalt.setGeometry(QtCore.QRect(160, 420, 571, 51))
        self.Rusalt.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";\n"
                                "color: rgb(0, 0, 0);\n"
                                "")
        self.Rusalt.setObjectName("Rusalt")
        self.UserName = QtWidgets.QLabel(Form)
        self.UserName.setGeometry(QtCore.QRect(60, 340, 351, 51))
        self.UserName.setStyleSheet("font: 75 18pt \"MS Shell Dlg 2\";\n"
                                   "color: rgb(0, 0, 0);")
        self.UserName.setText("")
        self.UserName.setAlignment(QtCore.Qt.AlignCenter)
        self.UserName.setObjectName("UserName")
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.Back.clicked.connect(self.BackMenu)
        self.Register.clicked.connect(self.RegisterUser)
        self.customer.clicked.connect(self.customerpage)
        self.seller.clicked.connect(self.sellerpage)

    def BackMenu(self):
          pass

    def RegisterUser(self):
          pass

    def customerpage(self):
          pass

    def sellerpage(self):
         pass
        
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.note.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">.برای ورود به سایت لطفا اطلاعات زیر را با دقت کامل کنید و رمزعبور خود را برای ورود به سایت به خاطر بسپارید</span></p></body></html>"))
        self.Password.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">رمز عبور</span></p></body></html>"))
        self.electronicWallet.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:9pt; font-weight:600;\">شارژ اولیه کیف پول</span></p></body></html>"))
        self.PhoneNumber.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">شماره تلفن</span></p></body></html>"))
        self.type.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">نوع کاربر</span></p></body></html>"))
        self.postalCode.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">کد پستی</span></p></body></html>"))
        self.mobile.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">شماره موبایل</span></p></body></html>"))
        self.Fristname.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600;\">نام</span></p></body></html>"))
        self.LastName.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">نام خانوادگی</span></p></body></html>"))
        self.seller.setText(_translate("Form", "فروشنده"))
        self.customer.setText(_translate("Form", "مشتری"))
        self.Back.setWhatsThis(_translate("Form", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.Rusalt.setText(_translate("Form", "<html><head/><body><p align=\"right\"><br/></p></body></html>"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Register()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())