# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\ProgramsPY\YTsave\main_interface.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(900, 500)
        Form.setLayoutDirection(QtCore.Qt.RightToLeft)
        Form.setStyleSheet("QWidget {\n"
"    background: #00F0FF;\n"
"}\n"
"\n"
"QFrame#frame{\n"
"    background: #00F0FF;\n"
"    background-image: url(:/Source/Frame.png);\n"
"    border: 1px solid #00F0FF;\n"
"}\n"
"\n"
"QLabel#lbl_save{\n"
"    font: 63 16pt \"Montserrat SemiBold\";\n"
"    background: #E1F2EB;\n"
"}\n"
"\n"
"\n"
"QLabel#lbl_description{\n"
"    font: 25 10pt \"Montserrat ExtraLight\";\n"
"    background: #E1F2EB;\n"
"    font-size: 13px;\n"
"}\n"
"\n"
"QLabel#lbl_description2{\n"
"    font: 25 10pt \"Montserrat ExtraLight\";\n"
"    background: #E1F2EB;\n"
"    font-size: 13px;\n"
"}\n"
"\n"
"QLineEdit#edt_link{\n"
"    background: #E1F2EB;\n"
"    border: none;\n"
"    border-bottom: 1px solid #1A7D84;\n"
"    font: 10pt \"Montserrat\";\n"
"}\n"
"\n"
"QPushButton#btn_download{\n"
"    font: 57 8pt \"Montserrat Medium\";\n"
"    color: #E5F3ED;\n"
"    background: #B4A3A3;\n"
"    border: 1px solid #D2C6C6;\n"
"    box-sizing: border-box;\n"
"    border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton#btn_download::hover{\n"
"    background: #C4C4C4;\n"
"}\n"
"\n"
"QLabel#lbl_image{\n"
"    background: #E1F2EB;\n"
"    background-image: url(:/Source/Illustration.png);\n"
"}\n"
"\n"
"QLabel#lbl_autor{\n"
"    background: #E1F2EB;\n"
"    font: 63 8pt \"Montserrat SemiBold\";\n"
"}")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setWindowTitle('PictureWorkshop');
        self.frame.setGeometry(QtCore.QRect(62, 75, 776, 350))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.lbl_save = QtWidgets.QLabel(self.frame)
        self.lbl_save.setGeometry(QtCore.QRect(401, 51, 274, 29))
        self.lbl_save.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_save.setObjectName("lbl_save")
        self.lbl_description = QtWidgets.QLabel(self.frame)
        self.lbl_description.setGeometry(QtCore.QRect(400, 90, 277, 18))
        self.lbl_description.setObjectName("lbl_description")
        self.lbl_description2 = QtWidgets.QLabel(self.frame)
        self.lbl_description2.setGeometry(QtCore.QRect(490, 111, 98, 18))
        self.lbl_description2.setObjectName("lbl_description2")
        self.edt_link = QtWidgets.QLineEdit(self.frame)
        self.edt_link.setGeometry(QtCore.QRect(430, 171, 221, 25))
        self.edt_link.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.edt_link.setTabletTracking(False)
        self.edt_link.setInputMask("")
        self.edt_link.setText("")
        self.edt_link.setCursorMoveStyle(QtCore.Qt.VisualMoveStyle)
        self.edt_link.setClearButtonEnabled(False)
        self.edt_link.setObjectName("edt_link")
        self.btn_download = QtWidgets.QPushButton(self.frame)
        self.btn_download.setGeometry(QtCore.QRect(460, 230, 162, 31))
        self.btn_download.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_download.setTabletTracking(False)
        self.btn_download.setObjectName("btn_download")
        self.lbl_image = QtWidgets.QLabel(self.frame)
        self.lbl_image.setGeometry(QtCore.QRect(100, 71, 241, 181))
        self.lbl_image.setText("")
        self.lbl_image.setObjectName("lbl_image")
        self.lbl_autor = QtWidgets.QLabel(self.frame)
        self.lbl_autor.setGeometry(QtCore.QRect(310, 290, 161, 16))
        self.lbl_autor.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lbl_autor.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_autor.setObjectName("lbl_autor")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.lbl_save.setText(_translate("Form", "Save video from Youtube"))
        self.lbl_description.setText(_translate("Form", "<html><head/><body><p align=\"center\">Paste the link from YouTube in the box and</p></body></html>"))
        self.lbl_description2.setText(_translate("Form", "<html><head/><body><p align=\"center\">click Download</p></body></html>"))
        self.edt_link.setPlaceholderText(_translate("Form", "Link for video"))
        self.btn_download.setText(_translate("Form", "Download"))
        self.lbl_autor.setText(_translate("Form", "Created by Bohdan Fesiuk"))
import ui_rc
