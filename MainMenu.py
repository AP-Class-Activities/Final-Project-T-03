from PyQt5 import QtCore, QtGui, QtWidgets

class MainMenu(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(648, 493)
        Form.setMaximumSize(QtCore.QSize(777, 777))
        self.Picture = QtWidgets.QLabel(Form)
        self.Picture.setGeometry(QtCore.QRect(0, 0, 701, 491))
        self.Picture.setMaximumSize(QtCore.QSize(701, 555))
        self.Picture.setText("")
        self.Picture.setPixmap(QtGui.QPixmap("Picture/main picture.jpg"))
        self.Picture.setObjectName("Picture")
        self.Welcome = QtWidgets.QLabel(Form)
        self.Welcome.setGeometry(QtCore.QRect(30, 20, 341, 51))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.Welcome.setFont(font)
        self.Welcome.setStyleSheet("\n"
                                "border-radius:20%;\n"
                                "\n"
                                "font: 75 18pt \"MS Shell Dlg 2\";\n"
                                "\n"
                                "color: rgb(0, 0, 0);\n"
                                "")
        self.Welcome.setAlignment(QtCore.Qt.AlignCenter)
        self.Welcome.setObjectName("Welcome")
        self.gridLayoutWidget = QtWidgets.QWidget(Form)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(-60, 80, 401, 161))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.Register = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.Register.setMinimumSize(QtCore.QSize(5, 40))
        self.Register.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(6, 128, 133, 255), stop:1 rgba(255, 255, 255, 255));\n"
                                        "border-radius:20%;\n"
                                        "\n"
                                        "border:1px solid  rgb(0, 0, 0);\n"
                                        "\n"
                                        "font: 75 22pt \"MS Shell Dlg 2\";\n"
                                        "color: rgb(0, 0, 0);\n"
                                        "")
        self.Register.setObjectName("Register")
        self.gridLayout.addWidget(self.Register, 3, 0, 1, 1)
        self.Free_User = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.Free_User.setMinimumSize(QtCore.QSize(0, 40))
        self.Free_User.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(6, 128, 133, 255), stop:1 rgba(255, 255, 255, 255));\n"
                                        "border-radius:20%;\n"
                                        "\n"
                                        "border:1px solid  rgb(0, 0, 0);\n"
                                        "\n"
                                        "font: 75 22pt \"MS Shell Dlg 2\";\n"
                                        "color: rgb(0, 0, 0);\n"
                                        "")
        self.Free_User.setDefault(False)
        self.Free_User.setFlat(False)
        self.Free_User.setObjectName("Free_User")
        self.gridLayout.addWidget(self.Free_User, 0, 0, 1, 1)
        self.Login = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.Login.setMinimumSize(QtCore.QSize(10, 40))
        self.Login.setMaximumSize(QtCore.QSize(250, 16777215))
        self.Login.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(6, 128, 133, 255), stop:1 rgba(255, 255, 255, 255));\n"
                                "border-radius:20%;\n"
                                "\n"
                                "border:1px solid  rgb(0, 0, 0);\n"
                                "\n"
                                "font: 75 22pt \"MS Shell Dlg 2\";\n"
                                "color: rgb(0, 0, 0);")
        self.Login.setObjectName("Login")
        self.gridLayout.addWidget(self.Login, 1, 0, 1, 1)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.Form=Form
        self.Free_User.clicked.connect(self.FreeUserMenu)
        self.Login.clicked.connect(self.Loginmenu)
        self.Register.clicked.connect(self.Registermenu)

    def FreeUserMenu(self):
        # با این کلید کاربر آزاد باید به صفحه محصولات منتقل شود
        pass

    def Loginmenu(self):
        # با این کلید کاربر به صفحه ورود وصل می شود
        self.Window = QtWidgets.QWidget() 
        self.ui = LoginPage()
        self.ui.setupUi(self.Window)
        Form.hide()
        self.Window.show()
        self.Form.close()

    def Registermenu(self):
        self.Window = QtWidgets.QWidget() 
        self.ui = Register()
        self.ui.setupUi(self.Window)
        Form.hide()
        self.Window.show()
        self.Form.close()

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "MainMenu"))
        self.Welcome.setText(_translate("Form", "<html><head/><body><p align=\"center\">.به فروشگاه ساحل خوش آمدید</p></body></html>"))
        self.Register.setText(_translate("Form", "ثبت نام"))
        self.Free_User.setText(_translate("Form", "کاربر آزاد"))
        self.Login.setText(_translate("Form", "ورود"))

class LoginPage(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(618, 542)
        Form.setMaximumSize(QtCore.QSize(777, 777))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        Form.setFont(font)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(0, 0, 621, 541))
        self.label.setMinimumSize(QtCore.QSize(20, 20))
        self.label.setMaximumSize(QtCore.QSize(650, 600))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("Picture/Login picture.jpg"))
        self.label.setObjectName("label")
        self.LoginUser = QtWidgets.QLabel(Form)
        self.LoginUser.setGeometry(QtCore.QRect(430, 0, 191, 81))
        self.LoginUser.setAlignment(QtCore.Qt.AlignCenter)
        self.LoginUser.setObjectName("LoginUser")
        self.gridLayoutWidget = QtWidgets.QWidget(Form)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 90, 601, 151))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.UsernameLine = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.UsernameLine.setMaximumSize(QtCore.QSize(16777215, 40))
        self.UsernameLine.setMaxLength(8)
        self.UsernameLine.setObjectName("UsernameLine")
        self.gridLayout.addWidget(self.UsernameLine, 0, 0, 1, 1)
        self.Username = QtWidgets.QLabel(self.gridLayoutWidget)
        self.Username.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(8, 192, 209, 255), stop:1 rgba(255, 255, 255, 255));\n"
                                        "font: 75 12pt \"MS Shell Dlg 2\";")
        self.Username.setObjectName("Username")
        self.gridLayout.addWidget(self.Username, 0, 1, 1, 1)
        self.PasswordLine = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.PasswordLine.setMaximumSize(QtCore.QSize(16777215, 40))
        self.PasswordLine.setMaxLength(8)
        self.PasswordLine.setEchoMode(QtWidgets.QLineEdit.Password)
        self.PasswordLine.setObjectName("PasswordLine")
        self.gridLayout.addWidget(self.PasswordLine, 1, 0, 1, 1)
        self.Password = QtWidgets.QLabel(self.gridLayoutWidget)
        self.Password.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(8, 192, 209, 255), stop:1 rgba(255, 255, 255, 255));\n"
                                        "font: 75 12pt \"MS Shell Dlg 2\";")
        self.Password.setObjectName("Password")
        self.gridLayout.addWidget(self.Password, 1, 1, 1, 1)
        self.Back = QtWidgets.QPushButton(Form)
        self.Back.setGeometry(QtCore.QRect(10, 10, 51, 51))
        self.Back.setStyleSheet("background-color: qconicalgradient(cx:0.5, cy:0.5, angle:0, stop:0 rgba(35, 40, 3, 255), stop:0.16 rgba(136, 106, 22, 255), stop:0.225 rgba(166, 140, 41, 255), stop:0.285 rgba(204, 181, 74, 255), stop:0.345 rgba(235, 219, 102, 255), stop:0.415 rgba(245, 236, 112, 255), stop:0.52 rgba(209, 190, 76, 255), stop:0.57 rgba(187, 156, 51, 255), stop:0.635 rgba(168, 142, 42, 255), stop:0.695 rgba(202, 174, 68, 255), stop:0.75 rgba(218, 202, 86, 255), stop:0.815 rgba(208, 187, 73, 255), stop:0.88 rgba(187, 156, 51, 255), stop:0.935 rgba(137, 108, 26, 255), stop:1 rgba(35, 40, 3, 255));\n"
                                "font: 75 16pt \"MS Shell Dlg 2\";\n"
                                "color: rgb(255, 255, 255);")
        self.Back.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon/Back.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Back.setIcon(icon)
        self.Back.setIconSize(QtCore.QSize(50, 50))
        self.Back.setObjectName("Back")
        self.Login = QtWidgets.QPushButton(Form)
        self.Login.setGeometry(QtCore.QRect(10, 460, 101, 71))
        self.Login.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                "font: 75 16pt \"MS Shell Dlg 2\";\n"
                                "color: rgb(255, 255, 255);")
        self.Login.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icon/login.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Login.setIcon(icon1)
        self.Login.setIconSize(QtCore.QSize(70, 70))
        self.Login.setObjectName("Login")
        self.Result = QtWidgets.QLabel(Form)
        self.Result.setGeometry(QtCore.QRect(180, 460, 431, 61))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.Result.setFont(font)
        self.Result.setStyleSheet("font: 75 20pt \"MS Shell Dlg 2\";\n"
                                "color: rgb(255, 255, 0);")
        self.Result.setAlignment(QtCore.Qt.AlignCenter)
        self.Result.setObjectName("Result")
        self.commentUsername = QtWidgets.QCommandLinkButton(Form)
        self.commentUsername.setGeometry(QtCore.QRect(10, 300, 601, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.commentUsername.setFont(font)
        self.commentUsername.setStyleSheet("background-color: qconicalgradient(cx:0.5, cy:0.5, angle:0, stop:0 rgba(200, 139, 139, 255), stop:1 rgba(255, 255, 255, 255));")
        self.commentUsername.setDefault(False)
        self.commentUsername.setObjectName("commentUsername")
        self.ForgetPassword = QtWidgets.QPushButton(Form)
        self.ForgetPassword.setGeometry(QtCore.QRect(10, 250, 601, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.ForgetPassword.setFont(font)
        self.ForgetPassword.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";\n"
                                        "color: rgb(255, 12, 36);")
        self.ForgetPassword.setObjectName("ForgetPassword")
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.Form=Form
        self.Back.clicked.connect(self.BackMenu)
        self.ForgetPassword.clicked.connect(self.ForgetPasswordmenu)
        self.Login.clicked.connect(self.Loginmenu)

    def BackMenu(self):
        self.Window = QtWidgets.QWidget() 
        self.ui = MainMenu()
        self.ui.setupUi(self.Window)
        self.Window.show()  
        self.Form.close()
            
    def ForgetPasswordmenu(self):
        self.Window = QtWidgets.QWidget() 
        self.ui = Forget()
        self.ui.setupUi(self.Window)
        Form.hide()
        self.Window.show()
        self.Form.close()  

    def Loginmenu(self):
        users = open("Database/database.txt","r")
        users = users.readlines()
        users = [u.replace('\n','').split() for u in users]
        f = False
        for i in range(0,len(users)):
            for j in range(0,len(users[i])):
                if users[i][j] == self.UsernameLine.text() and  users[i][j+1] == self.PasswordLine.text():
                   f = True
                        # بررسی یوزرنیم
                        # اگر یوزنیم موجود با زع شروع شود باید به صفحه مشتری برود
                        # در غیر این صورت به صفحه فروشنده میرود
                   self.Result.setStyleSheet('color:green;')
                   self.Result.setText('ورود با موفقیت انجام شد. :)')
                   break
        if f==False:
           self.Window = QtWidgets.QWidget() 
           self.ui = Register()
           self.ui.setupUi(self.Window)
           Form.hide()
           self.Window.show()
           self.Form.close() 
  

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Login Page"))
        self.LoginUser.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:24pt;\">ورود کاربر</span></p></body></html>"))
        self.Username.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">نام کاربری</span></p></body></html>"))
        self.Password.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">رمز عبور</span></p></body></html>"))
        self.Result.setText(_translate("Form", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.commentUsername.setText(_translate("Form", ".نام کاربری همان نامی است که به عنوان فروشنده یا مشتری به هنگام ثبت نام دریافت کرده اید"))
        self.ForgetPassword.setText(_translate("Form", ".در صورت فراموشی رمز عبور اینجا کلیک کنید"))

class Forget(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(602, 485)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(0, 0, 601, 481))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("Picture/Forget picture.jpg"))
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
        icon.addPixmap(QtGui.QPixmap("icon/Confirm.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
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
        icon1.addPixmap(QtGui.QPixmap("icon/Back.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
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
        icon2.addPixmap(QtGui.QPixmap("icon/risk.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
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
        icon3.addPixmap(QtGui.QPixmap("icon/register.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Register.setIcon(icon3)
        self.Register.setIconSize(QtCore.QSize(50, 50))
        self.Register.setObjectName("Register")
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.Form=Form
        self.BackToLogin.clicked.connect(self.BackToLoginpage)
        self.Confirm.clicked.connect(self.PasswordRecovery)
        self.Register.clicked.connect(self.RegisterUser)

    def BackToLoginpage(self):
        self.Window = QtWidgets.QWidget() 
        self.ui = LoginPage()
        self.ui.setupUi(self.Window)
        Form.hide()
        self.Window.show()
        self.Form.close()

    def PasswordRecovery(self):
        users = open("Database/database.txt","r")
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

    def RegisterUser(self):
        self.Window = QtWidgets.QWidget() 
        self.ui = Register()
        self.ui.setupUi(self.Window)
        Form.hide()
        self.Window.show()
        self.Form.close()

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Forget Page"))
        self.label_2.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600;\">بازیابی کلمه عبور</span></p></body></html>"))
        self.label_3.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">نام کاربری</span></p></body></html>"))
        self.label_4.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">رمز عبور شما</span></p></body></html>"))
        self.password.setText(_translate("Form", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.commandLinkButton.setText(_translate("Form", ".در صورت دریافت رمز عبور لطفا رمز عبور خود را به خاطر بسپارید"))
        self.Register.setText(_translate("Form", ".برای ثبت نام اینجا کلیک کنید"))

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
        icon.addPixmap(QtGui.QPixmap("icon/register.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
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
        icon1.addPixmap(QtGui.QPixmap("icon/Back.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
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
        self.Form=Form
        self.Back.clicked.connect(self.BackMenu)
        self.Register.clicked.connect(self.RegisterUser)
        self.customer.clicked.connect(self.customerpage)
        self.seller.clicked.connect(self.sellerpage)

    def BackMenu(self):
        self.Window = QtWidgets.QWidget() 
        self.ui = MainMenu()
        self.ui.setupUi(self.Window)
        Form.hide()
        self.Window.show()
        self.Form.close()

    def RegisterUser(self):
        #     دیتا از لیست ثبت نام مشتری ها باید ایجاد شود
        pass

    def customerpage(self): 
        # در صورت انتخاب این باتن فایل دیتا باز شود 
        #  و6 رقم اول با دو حرف اول مشتری به عنوان یوزنیم به کاربر داده شود
        pass

    def sellerpage(self):
        #    در صورت انتخاب این باتن فایل دیتا باز شود 
        #  و6 رقم اول با دو حرف اول فروشنده به عنوان یوزنیم به کاربر داده شود
        pass
        
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Register"))
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
    ui =  MainMenu()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())