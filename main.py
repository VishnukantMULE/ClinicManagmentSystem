

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("APSIT ClinicManagmetSystem-Dashbord")
        Form.resize(1001, 708)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QtCore.QSize(0, 10))
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(-10, 0, 1011, 711))
        self.frame.setSizeIncrement(QtCore.QSize(0, 0))
        self.frame.setTabletTracking(False)
        self.frame.setAcceptDrops(False)
        self.frame.setAutoFillBackground(False)
        self.frame.setStyleSheet("QFrame\n"
"{\n"
"    background-image: url(:/newPrefix/D:/Raw/v870-tang-35.jpg);\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(300, -10, 441, 131))
        self.label.setMinimumSize(QtCore.QSize(0, 0))
        self.label.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label.setScaledContents(False)
        self.label.setIndent(0)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(710, 440, 251, 61))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(255, 156, 35);\n"
"border-color: rgb(0, 0, 0);\n"
"border-style: outset;\n"
"border-width: 0.5px;")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(40, 440, 251, 61))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setToolTip("")
        self.pushButton_2.setStyleSheet("background-color: rgb(255, 156, 35);\n"
"border-color: rgb(0, 0, 0);\n"
"border-style: outset;\n"
"border-width: 0.5px;")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame)
        self.pushButton_3.setGeometry(QtCore.QRect(370, 560, 271, 61))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("background-color: rgb(85, 255, 0);\n"
"border-color: rgb(0, 0, 0);\n"
"border-style: outset;\n"
"border-width: 2px;")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_5 = QtWidgets.QPushButton(self.frame)
        self.pushButton_5.setGeometry(QtCore.QRect(710, 560, 251, 61))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("background-color: rgb(255, 156, 35);\n"
"border-color: rgb(0, 0, 0);\n"
"border-style: outset;\n"
"border-width: 0.5px;")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.frame)
        self.pushButton_6.setGeometry(QtCore.QRect(40, 560, 251, 61))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setStyleSheet("background-color: rgb(255, 156, 35);border-color: rgb(0, 0, 0);\n"
"border-style: outset;\n"
"border-width: 0.5px;")
        self.pushButton_6.setObjectName("pushButton_6")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(360, 140, 291, 381))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(":/newPrefix/D:/Raw/PinClipart.com_clinic-clip-art_5528315.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; font-weight:600;\">AP</span><span style=\" font-size:24pt; font-weight:600; color:#ff6347;\">S</span><span style=\" font-size:24pt; font-weight:600;\">IT</span><span style=\" font-size:26pt; vertical-align:sub;\">CLINIC MANAGMENT SYSTEM</span></p></body></html>"))
        self.pushButton.setText(_translate("Form", "Doctors Detail"))
        self.pushButton_2.setText(_translate("Form", "Doctor Login"))
        self.pushButton_3.setText(_translate("Form", "Book Apointment"))
        self.pushButton_5.setText(_translate("Form", "Clinic HIstory"))
        self.pushButton_6.setText(_translate("Form", "Admin Login"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
