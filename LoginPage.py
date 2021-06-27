
from PyQt5 import QtCore, QtGui, QtWidgets

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
        self.label.setPixmap(QtGui.QPixmap("www/Login picture.jpg"))
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
        icon.addPixmap(QtGui.QPixmap("Back.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
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
        icon1.addPixmap(QtGui.QPixmap("login.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
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

        self.Back.clicked.connect(self.BackMenu)
        self.ForgetPassword.clicked.connect(self.ForgetPasswordmenu)
        self.Login.clicked.connect(self.Loginmenu)

    def BackMenu(self):
        pass
            
    def ForgetPasswordmenu(sdlf):
        pass   

    def Loginmenu(sdlf):
        pass   

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Login Page"))
        self.LoginUser.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:24pt;\">ورود کاربر</span></p></body></html>"))
        self.Username.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">نام کاربری</span></p></body></html>"))
        self.Password.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">رمز عبور</span></p></body></html>"))
        self.Result.setText(_translate("Form", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.commentUsername.setText(_translate("Form", ".نام کاربری همان نامی است که به عنوان فروشنده یا مشتری به هنگام ثبت نام دریافت کرده اید"))
        self.ForgetPassword.setText(_translate("Form", ".در صورت فراموشی رمز عبور اینجا کلیک کنید"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = LoginPage()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())