# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CFSGSSBC.ui'
#
# Created: Sat Jan 19 15:13:35 2019
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(570, 393)
        self.label_5 = QtGui.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(20, 20, 541, 71))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Comic Sans MS"))
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.lineEdit_29 = QtGui.QLineEdit(Dialog)
        self.lineEdit_29.setGeometry(QtCore.QRect(370, 160, 191, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Poor Richard"))
        font.setPointSize(16)
        font.setItalic(True)
        self.lineEdit_29.setFont(font)
        self.lineEdit_29.setObjectName(_fromUtf8("lineEdit_29"))
        self.label_26 = QtGui.QLabel(Dialog)
        self.label_26.setGeometry(QtCore.QRect(20, 160, 321, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Stephen"))
        font.setPointSize(20)
        self.label_26.setFont(font)
        self.label_26.setObjectName(_fromUtf8("label_26"))
        self.lineEdit_30 = QtGui.QLineEdit(Dialog)
        self.lineEdit_30.setGeometry(QtCore.QRect(370, 220, 191, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Poor Richard"))
        font.setPointSize(16)
        font.setItalic(True)
        self.lineEdit_30.setFont(font)
        self.lineEdit_30.setObjectName(_fromUtf8("lineEdit_30"))
        self.label_27 = QtGui.QLabel(Dialog)
        self.label_27.setGeometry(QtCore.QRect(20, 220, 321, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Stephen"))
        font.setPointSize(20)
        self.label_27.setFont(font)
        self.label_27.setObjectName(_fromUtf8("label_27"))
        self.lineEdit_31 = QtGui.QLineEdit(Dialog)
        self.lineEdit_31.setGeometry(QtCore.QRect(370, 280, 191, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Poor Richard"))
        font.setPointSize(16)
        font.setItalic(True)
        self.lineEdit_31.setFont(font)
        self.lineEdit_31.setObjectName(_fromUtf8("lineEdit_31"))
        self.label_28 = QtGui.QLabel(Dialog)
        self.label_28.setGeometry(QtCore.QRect(20, 280, 321, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Stephen"))
        font.setPointSize(20)
        self.label_28.setFont(font)
        self.label_28.setObjectName(_fromUtf8("label_28"))
        self.lineEdit_32 = QtGui.QLineEdit(Dialog)
        self.lineEdit_32.setGeometry(QtCore.QRect(370, 100, 191, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Poor Richard"))
        font.setPointSize(16)
        font.setItalic(True)
        self.lineEdit_32.setFont(font)
        self.lineEdit_32.setObjectName(_fromUtf8("lineEdit_32"))
        self.label_29 = QtGui.QLabel(Dialog)
        self.label_29.setGeometry(QtCore.QRect(20, 100, 331, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Stephen"))
        font.setPointSize(20)
        self.label_29.setFont(font)
        self.label_29.setObjectName(_fromUtf8("label_29"))
        self.pushButton_3 = QtGui.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(330, 110, 31, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Pirate"))
        font.setPointSize(16)
        font.setItalic(True)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.pushButton = QtGui.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(10, 330, 271, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Pirate"))
        font.setPointSize(16)
        font.setItalic(True)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(290, 330, 271, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Pirate"))
        font.setPointSize(16)
        font.setItalic(True)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.label_5.setText(_translate("Dialog", "Salary Bonus Calculator", None))
        self.label_26.setText(_translate("Dialog", "Bonus percentage :", None))
        self.label_27.setText(_translate("Dialog", "Bonus (in Rs.) :", None))
        self.label_28.setText(_translate("Dialog", "Total Salary (in Rs.) :", None))
        self.label_29.setText(_translate("Dialog", "Employee ID :", None))
        self.pushButton_3.setText(_translate("Dialog", "...", None))
        self.pushButton.setText(_translate("Dialog", "Go back to menu", None))
        self.pushButton_2.setText(_translate("Dialog", "Save", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

