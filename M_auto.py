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
class Ui_Menu(object):
    def setupUi(self, Menu):
        Menu.setObjectName(_fromUtf8("Menu"))
        Menu.resize(431, 403)
        self.centralwidget = QtGui.QWidget(Menu)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.btn_CFT = QtGui.QPushButton(self.centralwidget)
        self.btn_CFT.setGeometry(QtCore.QRect(20, 150, 381, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Pirate"))
        font.setPointSize(16)
        font.setItalic(True)
        self.btn_CFT.setFont(font)
        self.btn_CFT.setObjectName(_fromUtf8("btn_CFT"))
        self.lbl_shallgivesalary = QtGui.QLabel(self.centralwidget)
        self.lbl_shallgivesalary.setGeometry(QtCore.QRect(10, 70, 401, 71))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Comic Sans MS"))
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_shallgivesalary.setFont(font)
        self.lbl_shallgivesalary.setObjectName(_fromUtf8("lbl_shallgivesalary"))
        self.btn_EDB = QtGui.QPushButton(self.centralwidget)
        self.btn_EDB.setGeometry(QtCore.QRect(20, 290, 381, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Pirate"))
        font.setPointSize(16)
        font.setItalic(True)
        self.btn_EDB.setFont(font)
        self.btn_EDB.setObjectName(_fromUtf8("btn_EDB"))
        self.lbl_carbonfootprint = QtGui.QLabel(self.centralwidget)
        self.lbl_carbonfootprint.setGeometry(QtCore.QRect(10, 10, 401, 71))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Comic Sans MS"))
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_carbonfootprint.setFont(font)
        self.lbl_carbonfootprint.setObjectName(_fromUtf8("lbl_carbonfootprint"))
        self.btn_SBC = QtGui.QPushButton(self.centralwidget)
        self.btn_SBC.setGeometry(QtCore.QRect(20, 220, 381, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Pirate"))
        font.setPointSize(16)
        font.setItalic(True)
        self.btn_SBC.setFont(font)
        self.btn_SBC.setObjectName(_fromUtf8("btn_SBC"))
        Menu.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(Menu)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 431, 26))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        Menu.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(Menu)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        Menu.setStatusBar(self.statusbar)
        self.retranslateUi(Menu)
        QtCore.QMetaObject.connectSlotsByName(Menu)
    def retranslateUi(self, Menu):
        Menu.setWindowTitle(_translate("Menu", "MainWindow", None))
        self.btn_CFT.setText(_translate("Menu", "Carbon Footprint Tracker", None))
        self.lbl_shallgivesalary.setText(_translate("Menu", "Shall Give Salary", None))
        self.btn_EDB.setText(_translate("Menu", "Employee Database", None))
        self.lbl_carbonfootprint.setText(_translate("Menu", "Carbon Footprint", None))
        self.btn_SBC.setText(_translate("Menu", "Salary Bonus Calculator", None))
if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Menu = QtGui.QMainWindow()
    ui = Ui_Menu()
    ui.setupUi(Menu)
    Menu.show()
    sys.exit(app.exec_())

