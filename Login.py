'''
Form implementation generated from reading ui file 'Login1.ui'
Created by: PyQt5 UI code generator 5.9.2
WARNING! All changes made in this file will be lost!
'''

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setWindowModality(QtCore.Qt.NonModal)
        Form.resize(560, 441)
        Form.setStyleSheet("background-color: qlineargradient(spread:reflect, x1:0.16, y1:0, x2:1, y2:1, stop:0 rgba(110, 166, 187, 255), stop:1 rgba(255, 255, 255, 255));\n"
                           "background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(201, 87, 28, 255), stop:0.55 rgba(235, 148, 61, 255), stop:0.98 rgba(0, 0, 0, 255), stop:1 rgba(0, 0, 0, 0));\n"
                           "background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(117, 185, 255, 255), stop:1 rgba(255, 255, 255, 255));")
        self.gridLayoutWidget = QtWidgets.QWidget(Form)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 60, 521, 231))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout.setContentsMargins(10, 10, 10, 10)
        self.gridLayout.setSpacing(10)
        self.gridLayout.setObjectName("gridLayout")
        self.PassLine = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.PassLine.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.PassLine.setFont(font)
        self.PassLine.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                    "border: 1px solid rgb(0, 0, 0);")
        self.PassLine.setEchoMode(QtWidgets.QLineEdit.Password)
        self.PassLine.setCursorPosition(0)
        self.PassLine.setObjectName("PassLine")
        self.gridLayout.addWidget(self.PassLine, 1, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setMaximumSize(QtCore.QSize(600, 40))
        self.label_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                   "font: 75 16pt \"MS Shell Dlg 2\";\n"
                                   "font: 16pt \"MS Shell Dlg 2\";\n"
                                   "border: 1px solid rgb(0, 0, 0);")
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setMinimumSize(QtCore.QSize(40, 40))
        self.label.setMaximumSize(QtCore.QSize(800, 800))
        self.label.setStyleSheet("background-color: qconicalgradient(cx:0.5, cy:0.5, angle:0, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(255, 255, 255, 255));\n"
                                 "font: 75 14pt \"MS Shell Dlg 2\";\n"
                                 " border: 1px solid  rgb(0, 0, 0);")
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)
        self.UserLine = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.UserLine.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.UserLine.setFont(font)
        self.UserLine.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                    "border: 1px solid rgb(0, 0, 0);")
        self.UserLine.setText("")
        self.UserLine.setObjectName("UserLine")
        self.gridLayout.addWidget(self.UserLine, 0, 0, 1, 1)
        self.Login = QtWidgets.QPushButton(Form)
        self.Login.setGeometry(QtCore.QRect(0, 300, 91, 51))
        self.Login.setMinimumSize(QtCore.QSize(91, 51))
        self.Login.setStyleSheet("font: 75 16pt \"MS Shell Dlg 2\";\n"
                                "color: rgb(170, 0, 0);\n"
                                "\n"
                                "border-radius: 12%;\n"
                                "border: 1px solid rgb(0, 0, 0);\n"
                                "\n"
                                "background-color: qconicalgradient(cx:0, cy:0, angle:135, stop:0 rgba(255, 255, 0, 69), stop:0.375 rgba(255, 255, 0, 69), stop:0.423533 rgba(251, 255, 0, 145), stop:0.45 rgba(247, 255, 0, 208), stop:0.477581 rgba(255, 244, 71, 130), stop:0.518717 rgba(255, 218, 71, 130), stop:0.55 rgba(255, 255, 0, 255), stop:0.57754 rgba(255, 203, 0, 130), stop:0.625 rgba(255, 255, 0, 69), stop:1 rgba(255, 255, 0, 69));\n"
                                "\n"
                                "font: 75 20pt \"MS Shell Dlg 2\";\n"
                                "color: rgb(170, 0, 0);\n"
                                "\n"
                                "")
        self.Login.setObjectName("Login")
        self.Login.clicked.connect(self.loginaccount)
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(170, 10, 241, 51))
        self.label_3.setStyleSheet("background-color: qconicalgradient(cx:0.5, cy:0.5, angle:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
                                   "background-color: qconicalgradient(cx:0, cy:0, angle:135, stop:0 rgba(255, 255, 0, 69), stop:0.375 rgba(255, 255, 0, 69), stop:0.423533 rgba(251, 255, 0, 145), stop:0.45 rgba(247, 255, 0, 208), stop:0.477581 rgba(255, 244, 71, 130), stop:0.518717 rgba(255, 218, 71, 130), stop:0.55 rgba(255, 255, 0, 255), stop:0.57754 rgba(255, 203, 0, 130), stop:0.625 rgba(255, 255, 0, 69), stop:1 rgba(255, 255, 0, 69));\n"
                                   "font: 75 16pt \"MS Shell Dlg 2\";\n"
                                   "color: rgb(170, 0, 0);\n"
                                   "\n"
                                   "border-radius: 12%;\n"
                                   "border: 1px solid rgb(0, 0, 0);")
        self.label_3.setObjectName("label_3")
        self.LogLabel = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.LogLabel.setFont(font)
        self.LogLabel.setGeometry(QtCore.QRect(220, 350, 321, 51))
        self.LogLabel.setObjectName("LogLabel")
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def loginaccount(self):
        username = self.UserLine.text()
        password = self.PassLine.text()
        users = open("database.txt","r")
        users = users.readlines()
        users = [u.replace('\n','').split() for u in users]
        l = False
        for i in range(len(users)):
                if username == users[i][0]  and password == users[i][1]:
                        l = True
                        self.LogLabel.setText('{} خوش آمدید. :)'.format(users[i][0]))
                        break
        if l == False:
              self.LogLabel.setText('نام کاربری یا پسورد نامعتبر است. :(')  
             
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "log in"))
        self.label_2.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">پسورد</span></p></body></html>"))
        self.label.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">نام کاربری</span></p></body></html>"))
        self.Login.setText(_translate("Form", "ورود"))
        self.label_3.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600;\">ورود کاربر</span></p></body></html>"))
        self.LogLabel.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">TextLabel</span></p></body></html>"))

if __name__ == "__main__":
    import sys 
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())