from LoginPage import LoginPage
from PyQt5 import QtCore, QtGui, QtWidgets

class Forget(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(602, 485)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(0, 0, 601, 481))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("www/Forget picture.jpg"))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(330, 20, 311, 81))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(430, 100, 161, 50))
        self.label_3.setMaximumSize(QtCore.QSize(16777215, 50))
        self.label_3.setStyleSheet("background-color: rgb(219, 207, 255);\n"
                                "border: 1px solid rgb(0, 0, 0);\n"
                                "font: 75 14pt \"MS Shell Dlg 2\";\n"
                                "")
        self.label_3.setObjectName("label_3")
        self.lineEditname = QtWidgets.QLineEdit(Form)
        self.lineEditname.setGeometry(QtCore.QRect(60, 100, 361, 50))
        self.lineEditname.setMaximumSize(QtCore.QSize(16777215, 50))
        self.lineEditname.setStyleSheet("font: 75 16pt \"MS Shell Dlg 2\";")
        self.lineEditname.setObjectName("lineEditname")
        self.Confirm = QtWidgets.QPushButton(Form)
        self.Confirm.setGeometry(QtCore.QRect(10, 180, 51, 50))
        self.Confirm.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.Confirm.setFont(font)
        self.Confirm.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Confirm.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Confirm.setIcon(icon)
        self.Confirm.setIconSize(QtCore.QSize(44, 44))
        self.Confirm.setObjectName("Confirm")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(440, 240, 150, 50))
        self.label_4.setMinimumSize(QtCore.QSize(150, 50))
        self.label_4.setMaximumSize(QtCore.QSize(16777215, 50))
        self.label_4.setStyleSheet("background-color: rgb(219, 207, 255);\n"
                                        "border: 1px solid rgb(0, 0, 0);\n"
                                        "font: 75 14pt \"MS Shell Dlg 2\";\n"
                                        "")
        self.label_4.setObjectName("label_4")
        self.password = QtWidgets.QLabel(Form)
        self.password.setGeometry(QtCore.QRect(90, 240, 331, 50))
        self.password.setMinimumSize(QtCore.QSize(150, 50))
        self.password.setMaximumSize(QtCore.QSize(16777215, 50))
        self.password.setStyleSheet("font: 75 24pt \"MS Shell Dlg 2\";\n"
                                "color: rgb(0, 0, 0);")
        self.password.setAlignment(QtCore.Qt.AlignCenter)
        self.password.setObjectName("password")
        self.BackToLogin = QtWidgets.QPushButton(Form)
        self.BackToLogin.setGeometry(QtCore.QRect(10, 10, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.BackToLogin.setFont(font)
        self.BackToLogin.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Back.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BackToLogin.setIcon(icon1)
        self.BackToLogin.setIconSize(QtCore.QSize(40, 40))
        self.BackToLogin.setObjectName("BackToLogin")
        self.commandLinkButton = QtWidgets.QCommandLinkButton(Form)
        self.commandLinkButton.setGeometry(QtCore.QRect(60, 320, 461, 41))
        self.commandLinkButton.setObjectName("commandLinkButton")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(530, 320, 51, 41))
        self.pushButton.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("risk.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon2)
        self.pushButton.setIconSize(QtCore.QSize(40, 40))
        self.pushButton.setObjectName("pushButton")
        self.Register = QtWidgets.QPushButton(Form)
        self.Register.setGeometry(QtCore.QRect(70, 400, 351, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.Register.setFont(font)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("register.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Register.setIcon(icon3)
        self.Register.setIconSize(QtCore.QSize(50, 50))
        self.Register.setObjectName("Register")
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.BackToLogin.clicked.connect(self.BackToLoginpage)
        self.Confirm.clicked.connect(self.PasswordRecovery)
        self.Register.clicked.connect(self.RegisterUser)

    def BackToLoginpage(self):
        self.Window = QtWidgets.QWidget() 
        self.ui = LoginPage()
        self.ui.setupUi(self.Window)
        Form.hide()
        self.Window.show()

    def PasswordRecovery(self):
        users = open("database.txt","r")
        users = users.readlines()
        users = [u.replace('\n','').split() for u in users]
        f = False
        for i in range(0,len(users)):
            for j in range(0,len(users[i])):
                    if users[i][j] == self.lineEditname.text():
                        f = True
                        newpassword = users[i][j+1]
                        self.password.setText(newpassword)
                        break
        if f==False:
            self.password.setText("لطفا ثبت نام کنید. :)")

    def   RegisterUser(self):
            print('sfd')    
        #   pass

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Forget Page"))
        self.label_2.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600;\">بازیابی کلمه عبور</span></p></body></html>"))
        self.label_3.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">نام کاربری</span></p></body></html>"))
        self.label_4.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">رمز عبور شما</span></p></body></html>"))
        self.password.setText(_translate("Form", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.commandLinkButton.setText(_translate("Form", ".در صورت دریافت رمز عبور لطفا رمز عبور خود را به خاطر بسپارید"))
        self.Register.setText(_translate("Form", ".برای ثبت نام اینجا کلیک کنید"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Forget()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())