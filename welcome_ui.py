# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'welcome_screen.ui'
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
        Dialog.setStyleSheet("QPushButton{\n"
"font: 20pt \"Consolas\";\n"
"background-color:rgb(201, 150, 204);\n"
"border-radius:15px;\n"
"border-color: rgb(84, 255, 5);\n"
"color:rgb(28, 12, 91);};\n"
"\n"
"")
        self.bgwidget = QtWidgets.QWidget(Dialog)
        self.bgwidget.setGeometry(QtCore.QRect(-1, -1, 1201, 801))
        self.bgwidget.setStyleSheet("QWidget#bgwidget{background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgb(28, 12, 91), stop:0.041 rgb(28, 12, 91), stop:1 rgb(145, 107, 191));;};\n"
"")
        self.bgwidget.setObjectName("bgwidget")
        self.label = QtWidgets.QLabel(self.bgwidget)
        self.label.setGeometry(QtCore.QRect(810, 20, 371, 112))
        self.label.setStyleSheet("font: 75 72pt \"Consolas\";\n"
"color: rgb(201, 150, 204);")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.bgwidget)
        self.label_2.setGeometry(QtCore.QRect(387, 130, 791, 47))
        self.label_2.setStyleSheet("font: 75 30pt \"Consolas\";\n"
"color: rgb(201, 150, 204);")
        self.label_2.setObjectName("label_2")
        self.signin_button = QtWidgets.QPushButton(self.bgwidget)
        self.signin_button.setGeometry(QtCore.QRect(810, 190, 181, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        self.signin_button.setFont(font)
        self.signin_button.setStyleSheet("")
        self.signin_button.setObjectName("signin_button")
        self.signup_button = QtWidgets.QPushButton(self.bgwidget)
        self.signup_button.setGeometry(QtCore.QRect(1000, 190, 181, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        self.signup_button.setFont(font)
        self.signup_button.setStyleSheet("")
        self.signup_button.setObjectName("signup_button")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Welcome"))
        self.label_2.setText(_translate("Dialog", "Sign in or Sign up for a new account"))
        self.signin_button.setText(_translate("Dialog", "Sign in"))
        self.signup_button.setText(_translate("Dialog", "Sign up"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
