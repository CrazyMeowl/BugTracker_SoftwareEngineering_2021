# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'popup.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(600, 130)
        Dialog.setMinimumSize(QtCore.QSize(600, 130))
        Dialog.setMaximumSize(QtCore.QSize(600, 130))
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(0, 0, 1001, 411))
        self.widget.setStyleSheet("background-color: rgb(17, 60, 74);")
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(10, -10, 521, 71))
        self.label.setStyleSheet("font: 500 italic 20pt \"Ubuntu\";\n"
"color: rgb(221, 221, 221);")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(30, 40, 471, 31))
        self.label_2.setStyleSheet("font: 500 italic 20pt \"Ubuntu\";\n"
"color: rgb(221, 221, 221);")
        self.label_2.setObjectName("label_2")
        self.email_button = QtWidgets.QPushButton(self.widget)
        self.email_button.setGeometry(QtCore.QRect(40, 80, 501, 24))
        self.email_button.setStyleSheet("border:none;\n"
"font: 500 italic 20pt \"Ubuntu\";\n"
"color: rgb(246, 114, 128);")
        self.email_button.setObjectName("email_button")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Want to create a company ? "))
        self.label_2.setText(_translate("Dialog", "Contact us at :"))
        self.email_button.setText(_translate("Dialog", "ITITIU19185@student.hcmiu.edu.vn"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
