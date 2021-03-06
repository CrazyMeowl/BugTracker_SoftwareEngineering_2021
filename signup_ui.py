# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'signup_screen.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1200, 800)
        Dialog.setMinimumSize(QtCore.QSize(1200, 800))
        Dialog.setMaximumSize(QtCore.QSize(1200, 800))
        Dialog.setStyleSheet("QLineEdit{font: 20pt \"Consolas\";\n"
"background-color:rgb(145, 107, 191);\n"
"border-radius:15px;\n"
"border-color: rgb(84, 255, 5);\n"
"color: rgb(61, 44, 141);}\n"
"QPushButton{\n"
"font: 20pt \"Consolas\";\n"
"background-color:rgb(201, 150, 204);\n"
"border-radius:15px;\n"
"border-color: rgb(84, 255, 5);\n"
"color:rgb(28, 12, 91);};\n"
"\n"
"\n"
"\n"
"")
        self.bgwidget = QtWidgets.QWidget(Dialog)
        self.bgwidget.setGeometry(QtCore.QRect(0, -1, 1201, 801))
        self.bgwidget.setStyleSheet("QWidget#bgwidget{background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgb(28, 12, 91), stop:0.041 rgb(28, 12, 91), stop:1 rgb(145, 107, 191));;};\n"
"")
        self.bgwidget.setObjectName("bgwidget")
        self.label = QtWidgets.QLabel(self.bgwidget)
        self.label.setGeometry(QtCore.QRect(810, 20, 371, 112))
        self.label.setStyleSheet("font: 75 72pt \"Consolas\";\n"
"color: rgb(201, 150, 204);")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.bgwidget)
        self.label_2.setGeometry(QtCore.QRect(630, 130, 551, 47))
        self.label_2.setStyleSheet("font: 75 30pt \"Consolas\";\n"
"\n"
"color:rgb(201, 150, 204);\n"
"\n"
"")
        self.label_2.setObjectName("label_2")
        self.signup_button = QtWidgets.QPushButton(self.bgwidget)
        self.signup_button.setGeometry(QtCore.QRect(1030, 580, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        self.signup_button.setFont(font)
        self.signup_button.setStyleSheet("")
        self.signup_button.setObjectName("signup_button")
        self.username_box = QtWidgets.QLineEdit(self.bgwidget)
        self.username_box.setGeometry(QtCore.QRect(810, 370, 371, 41))
        self.username_box.setStyleSheet("")
        self.username_box.setObjectName("username_box")
        self.label_3 = QtWidgets.QLabel(self.bgwidget)
        self.label_3.setGeometry(QtCore.QRect(650, 380, 151, 31))
        self.label_3.setStyleSheet("color:rgb(201, 150, 204);\n"
"font: 75 25pt \"Consolas\";")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.bgwidget)
        self.label_4.setGeometry(QtCore.QRect(650, 450, 151, 31))
        self.label_4.setStyleSheet("color:rgb(201, 150, 204);\n"
"font: 75 25pt \"Consolas\";")
        self.label_4.setObjectName("label_4")
        self.password_box = QtWidgets.QLineEdit(self.bgwidget)
        self.password_box.setGeometry(QtCore.QRect(810, 440, 371, 41))
        self.password_box.setStyleSheet("")
        self.password_box.setObjectName("password_box")
        self.error = QtWidgets.QLabel(self.bgwidget)
        self.error.setGeometry(QtCore.QRect(560, 640, 621, 31))
        self.error.setStyleSheet("font: 75 15pt \"Consolas\"; color:red;")
        self.error.setText("")
        self.error.setObjectName("error")
        self.confirm_password_box = QtWidgets.QLineEdit(self.bgwidget)
        self.confirm_password_box.setGeometry(QtCore.QRect(810, 510, 371, 41))
        self.confirm_password_box.setStyleSheet("")
        self.confirm_password_box.setObjectName("confirm_password_box")
        self.label_5 = QtWidgets.QLabel(self.bgwidget)
        self.label_5.setGeometry(QtCore.QRect(510, 520, 291, 31))
        self.label_5.setStyleSheet("color:rgb(201, 150, 204);\n"
"\n"
"font: 75 25pt \"Consolas\";")
        self.label_5.setObjectName("label_5")
        self.back_button = QtWidgets.QPushButton(self.bgwidget)
        self.back_button.setGeometry(QtCore.QRect(10, 750, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        self.back_button.setFont(font)
        self.back_button.setStyleSheet("")
        self.back_button.setObjectName("back_button")
        self.create_company_button = QtWidgets.QPushButton(self.bgwidget)
        self.create_company_button.setGeometry(QtCore.QRect(480, 750, 701, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        self.create_company_button.setFont(font)
        self.create_company_button.setStyleSheet("")
        self.create_company_button.setObjectName("create_company_button")
        self.label_6 = QtWidgets.QLabel(self.bgwidget)
        self.label_6.setGeometry(QtCore.QRect(650, 310, 151, 31))
        self.label_6.setStyleSheet("color:rgb(201, 150, 204);\n"
"font: 75 25pt \"Consolas\";")
        self.label_6.setObjectName("label_6")
        self.fullname_box = QtWidgets.QLineEdit(self.bgwidget)
        self.fullname_box.setGeometry(QtCore.QRect(810, 300, 371, 41))
        self.fullname_box.setStyleSheet("")
        self.fullname_box.setObjectName("fullname_box")
        self.email_box = QtWidgets.QLineEdit(self.bgwidget)
        self.email_box.setGeometry(QtCore.QRect(810, 230, 371, 41))
        self.email_box.setStyleSheet("")
        self.email_box.setText("")
        self.email_box.setObjectName("email_box")
        self.label_7 = QtWidgets.QLabel(self.bgwidget)
        self.label_7.setGeometry(QtCore.QRect(700, 240, 91, 31))
        self.label_7.setStyleSheet("color:rgb(201, 150, 204);\n"
"font: 75 25pt \"Consolas\";")
        self.label_7.setObjectName("label_7")
        self.birthdate_box = QtWidgets.QDateEdit(self.bgwidget)
        self.birthdate_box.setGeometry(QtCore.QRect(810, 580, 201, 41))
        self.birthdate_box.setStyleSheet("QDateEdit{\n"
"font: 20pt \"Consolas\";\n"
"background-color:rgb(145, 107, 191);\n"
"border-radius:15px;\n"
"border-color: rgb(84, 255, 5);\n"
"color: rgb(61, 44, 141);};")
        self.birthdate_box.setAlignment(QtCore.Qt.AlignCenter)
        self.birthdate_box.setObjectName("birthdate_box")
        self.label_8 = QtWidgets.QLabel(self.bgwidget)
        self.label_8.setGeometry(QtCore.QRect(560, 590, 241, 31))
        self.label_8.setStyleSheet("color:rgb(201, 150, 204);\n"
"\n"
"font: 75 25pt \"Consolas\";")
        self.label_8.setObjectName("label_8")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Sign up"))
        self.label_2.setText(_translate("Dialog", "Sign up for a new account"))
        self.signup_button.setText(_translate("Dialog", "Sign up"))
        self.username_box.setPlaceholderText(_translate("Dialog", "abc123"))
        self.label_3.setText(_translate("Dialog", "Username"))
        self.label_4.setText(_translate("Dialog", "Password"))
        self.password_box.setPlaceholderText(_translate("Dialog", "password"))
        self.confirm_password_box.setPlaceholderText(_translate("Dialog", "password"))
        self.label_5.setText(_translate("Dialog", "Confirm password"))
        self.back_button.setText(_translate("Dialog", "Back"))
        self.create_company_button.setText(_translate("Dialog", "If you want to create as a company click this "))
        self.label_6.setText(_translate("Dialog", "Fullname"))
        self.fullname_box.setPlaceholderText(_translate("Dialog", "Peter Parker"))
        self.email_box.setPlaceholderText(_translate("Dialog", "abc@gmail.com"))
        self.label_7.setText(_translate("Dialog", "Email"))
        self.birthdate_box.setDisplayFormat(_translate("Dialog", "d/M/yyyy"))
        self.label_8.setText(_translate("Dialog", "Date of birth"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
