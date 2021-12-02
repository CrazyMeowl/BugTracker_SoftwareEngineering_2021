# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_menu_admin.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class MainMenuCustomerUi(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1200, 800)
        Dialog.setMinimumSize(QtCore.QSize(1200, 800))
        Dialog.setMaximumSize(QtCore.QSize(1200, 800))
        Dialog.setStyleSheet("QDialog#Dialog{\n"
"background-color:  rgb(125, 125, 125);\n"
"}\n"
"*{\n"
"    border : none;\n"
"    color: white;\n"
"    font: 75 10pt \"Consolas\";\n"
"}\n"
"QToolBox::tab{\n"
"    border-radius:5px;\n"
"    text-align:left;\n"
"}\n"
"\n"
"QToolBox{\n"
"    text-align: left;\n"
"    color: white;\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.horizontalLayout = QtWidgets.QHBoxLayout(Dialog)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.slide_menu_container = QtWidgets.QFrame(Dialog)
        self.slide_menu_container.setMaximumSize(QtCore.QSize(250, 16777215))
        self.slide_menu_container.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.slide_menu_container.setStyleSheet("background-color:rgb(107, 79, 79)\n"
"")
        self.slide_menu_container.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.slide_menu_container.setFrameShadow(QtWidgets.QFrame.Raised)
        self.slide_menu_container.setObjectName("slide_menu_container")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.slide_menu_container)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_2 = QtWidgets.QFrame(self.slide_menu_container)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.header = QtWidgets.QFrame(self.frame_2)
        self.header.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.header.setFrameShadow(QtWidgets.QFrame.Raised)
        self.header.setObjectName("header")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.header)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.pushButton_6 = QtWidgets.QPushButton(self.header)
        self.pushButton_6.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/activity.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_6.setIcon(icon)
        self.pushButton_6.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_6.setObjectName("pushButton_6")
        self.horizontalLayout_8.addWidget(self.pushButton_6)
        self.label_4 = QtWidgets.QLabel(self.header)
        self.label_4.setStyleSheet("color:rgb(255, 243, 228);\n"
"font: 75 22pt \"Consolas\";")
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_8.addWidget(self.label_4)
        self.verticalLayout_6.addWidget(self.header, 0, QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.side_menu_menu = QtWidgets.QFrame(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.side_menu_menu.sizePolicy().hasHeightForWidth())
        self.side_menu_menu.setSizePolicy(sizePolicy)
        self.side_menu_menu.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.side_menu_menu.setFrameShadow(QtWidgets.QFrame.Raised)
        self.side_menu_menu.setObjectName("side_menu_menu")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.side_menu_menu)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.toolBox = QtWidgets.QToolBox(self.side_menu_menu)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolBox.sizePolicy().hasHeightForWidth())
        self.toolBox.setSizePolicy(sizePolicy)
        self.toolBox.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.toolBox.setStyleSheet("")
        self.toolBox.setObjectName("toolBox")
        self.drop_menu_1 = QtWidgets.QWidget()
        self.drop_menu_1.setGeometry(QtCore.QRect(0, 0, 250, 674))
        self.drop_menu_1.setObjectName("drop_menu_1")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.drop_menu_1)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.frame = QtWidgets.QFrame(self.drop_menu_1)
        self.frame.setMaximumSize(QtCore.QSize(225, 16777215))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.pushButton_8 = QtWidgets.QPushButton(self.frame)
        self.pushButton_8.setObjectName("pushButton_8")
        self.verticalLayout_10.addWidget(self.pushButton_8)
        self.pushButton_9 = QtWidgets.QPushButton(self.frame)
        self.pushButton_9.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.pushButton_9.setObjectName("pushButton_9")
        self.verticalLayout_10.addWidget(self.pushButton_9)
        self.pushButton_7 = QtWidgets.QPushButton(self.frame)
        self.pushButton_7.setObjectName("pushButton_7")
        self.verticalLayout_10.addWidget(self.pushButton_7)
        self.verticalLayout_8.addWidget(self.frame, 0, QtCore.Qt.AlignTop)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/black/black/chevron-down.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolBox.addItem(self.drop_menu_1, icon1, "")
        self.Drop_menu_2 = QtWidgets.QWidget()
        self.Drop_menu_2.setGeometry(QtCore.QRect(0, 0, 250, 674))
        self.Drop_menu_2.setObjectName("Drop_menu_2")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.Drop_menu_2)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.frame_3 = QtWidgets.QFrame(self.Drop_menu_2)
        self.frame_3.setMaximumSize(QtCore.QSize(225, 16777215))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.pushButton_11 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_11.setObjectName("pushButton_11")
        self.verticalLayout_11.addWidget(self.pushButton_11)
        self.pushButton_10 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_10.setObjectName("pushButton_10")
        self.verticalLayout_11.addWidget(self.pushButton_10)
        self.pushButton_12 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_12.setObjectName("pushButton_12")
        self.verticalLayout_11.addWidget(self.pushButton_12)
        self.verticalLayout_9.addWidget(self.frame_3, 0, QtCore.Qt.AlignTop)
        self.label_5 = QtWidgets.QLabel(self.Drop_menu_2)
        self.label_5.setText("")
        self.label_5.setWordWrap(True)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_9.addWidget(self.label_5)
        self.toolBox.addItem(self.Drop_menu_2, icon1, "")
        self.verticalLayout_7.addWidget(self.toolBox)
        self.verticalLayout_6.addWidget(self.side_menu_menu)
        self.footer = QtWidgets.QFrame(self.frame_2)
        self.footer.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.footer.setFrameShadow(QtWidgets.QFrame.Raised)
        self.footer.setObjectName("footer")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.footer)
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.exit_button = QtWidgets.QPushButton(self.footer)
        self.exit_button.setStyleSheet("font: 20pt \"Consolas\";")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/icons/x.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.exit_button.setIcon(icon2)
        self.exit_button.setIconSize(QtCore.QSize(30, 30))
        self.exit_button.setObjectName("exit_button")
        self.horizontalLayout_9.addWidget(self.exit_button)
        self.verticalLayout_6.addWidget(self.footer, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignBottom)
        self.verticalLayout_2.addWidget(self.frame_2)
        self.horizontalLayout.addWidget(self.slide_menu_container)
        self.main_menu_container = QtWidgets.QFrame(Dialog)
        self.main_menu_container.setStyleSheet("background-color:rgb(72, 52, 52);")
        self.main_menu_container.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.main_menu_container.setFrameShadow(QtWidgets.QFrame.Raised)
        self.main_menu_container.setObjectName("main_menu_container")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.main_menu_container)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.header_frame = QtWidgets.QFrame(self.main_menu_container)
        self.header_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.header_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.header_frame.setObjectName("header_frame")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.header_frame)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.header_0 = QtWidgets.QFrame(self.header_frame)
        self.header_0.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.header_0.setFrameShadow(QtWidgets.QFrame.Raised)
        self.header_0.setObjectName("header_0")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.header_0)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.menu_buton = QtWidgets.QPushButton(self.header_0)
        self.menu_buton.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.menu_buton.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/icons/menu.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menu_buton.setIcon(icon3)
        self.menu_buton.setIconSize(QtCore.QSize(25, 25))
        self.menu_buton.setObjectName("menu_buton")
        self.horizontalLayout_7.addWidget(self.menu_buton, 0, QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.horizontalLayout_5.addWidget(self.header_0, 0, QtCore.Qt.AlignLeft)
        self.header_1 = QtWidgets.QFrame(self.header_frame)
        self.header_1.setMinimumSize(QtCore.QSize(0, 0))
        self.header_1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.header_1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.header_1.setObjectName("header_1")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.header_1)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.lineEdit = QtWidgets.QLineEdit(self.header_1)
        self.lineEdit.setStyleSheet("border-bottom:2px solid rgb(246, 174, 153);")
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_6.addWidget(self.lineEdit)
        self.pushButton_2 = QtWidgets.QPushButton(self.header_1)
        self.pushButton_2.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/icons/search.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon4)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_6.addWidget(self.pushButton_2)
        self.horizontalLayout_5.addWidget(self.header_1)
        self.header_2 = QtWidgets.QFrame(self.header_frame)
        self.header_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.header_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.header_2.setObjectName("header_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.header_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.header_2)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_2.addWidget(self.pushButton_3)
        self.pushButton = QtWidgets.QPushButton(self.header_2)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_2.addWidget(self.pushButton)
        self.horizontalLayout_5.addWidget(self.header_2)
        self.header_3 = QtWidgets.QFrame(self.header_frame)
        self.header_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.header_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.header_3.setObjectName("header_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.header_3)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.notify_button = QtWidgets.QPushButton(self.header_3)
        self.notify_button.setObjectName("notify_button")
        self.horizontalLayout_4.addWidget(self.notify_button)
        self.user_setting_button = QtWidgets.QPushButton(self.header_3)
        self.user_setting_button.setObjectName("user_setting_button")
        self.horizontalLayout_4.addWidget(self.user_setting_button)
        self.setting_button = QtWidgets.QPushButton(self.header_3)
        self.setting_button.setObjectName("setting_button")
        self.horizontalLayout_4.addWidget(self.setting_button)
        self.horizontalLayout_5.addWidget(self.header_3)
        self.verticalLayout.addWidget(self.header_frame, 0, QtCore.Qt.AlignTop)
        self.main_menu_content = QtWidgets.QFrame(self.main_menu_container)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main_menu_content.sizePolicy().hasHeightForWidth())
        self.main_menu_content.setSizePolicy(sizePolicy)
        self.main_menu_content.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.main_menu_content.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.main_menu_content.setFrameShadow(QtWidgets.QFrame.Raised)
        self.main_menu_content.setObjectName("main_menu_content")
        self.verticalLayout.addWidget(self.main_menu_content)
        self.footer_frame = QtWidgets.QFrame(self.main_menu_container)
        self.footer_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.footer_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.footer_frame.setObjectName("footer_frame")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.footer_frame)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.frame_8 = QtWidgets.QFrame(self.footer_frame)
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_8)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label = QtWidgets.QLabel(self.frame_8)
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label, 0, QtCore.Qt.AlignBottom)
        self.horizontalLayout_3.addWidget(self.frame_8)
        self.frame_7 = QtWidgets.QFrame(self.footer_frame)
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_7)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_2 = QtWidgets.QLabel(self.frame_7)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_4.addWidget(self.label_2)
        self.horizontalLayout_3.addWidget(self.frame_7)
        self.frame_9 = QtWidgets.QFrame(self.footer_frame)
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_9)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_3 = QtWidgets.QLabel(self.frame_9)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_5.addWidget(self.label_3)
        self.horizontalLayout_3.addWidget(self.frame_9)
        self.verticalLayout.addWidget(self.footer_frame, 0, QtCore.Qt.AlignBottom)
        self.horizontalLayout.addWidget(self.main_menu_container)

        self.retranslateUi(Dialog)
        self.toolBox.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_4.setText(_translate("Dialog", "Bug Tracker"))
        self.pushButton_8.setText(_translate("Dialog", "PushButton"))
        self.pushButton_9.setText(_translate("Dialog", "PushButton"))
        self.pushButton_7.setText(_translate("Dialog", "PushButton"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.drop_menu_1), _translate("Dialog", "Page 1"))
        self.pushButton_11.setText(_translate("Dialog", "PushButton"))
        self.pushButton_10.setText(_translate("Dialog", "PushButton"))
        self.pushButton_12.setText(_translate("Dialog", "PushButton"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.Drop_menu_2), _translate("Dialog", "Page 2"))
        self.exit_button.setText(_translate("Dialog", "Exit "))
        self.pushButton_3.setText(_translate("Dialog", "PushButton"))
        self.pushButton.setText(_translate("Dialog", "PushButton"))
        self.notify_button.setText(_translate("Dialog", "PushButton"))
        self.user_setting_button.setText(_translate("Dialog", "PushButton"))
        self.setting_button.setText(_translate("Dialog", "PushButton"))
        self.label.setText(_translate("Dialog", "placeholder"))
        self.label_2.setText(_translate("Dialog", "placeholder"))
        self.label_3.setText(_translate("Dialog", "placeholder"))
import icons_rc