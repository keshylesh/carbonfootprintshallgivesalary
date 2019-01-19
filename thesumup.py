import sys
from PyQt4 import QtCore, QtGui, uic
import sqlite3
from everything_auto import *
class Ui_Dialog(QtGui.QMainWindow, Ui_Dialog):
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.conn = sqlite3.connect("CFSGSDB.db")
        QtGui.QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.lne_TCF.setReadOnly(True)
        self.lne_bonuspc.setReadOnly(True)
        self.lne_bonusmon.setReadOnly(True)
        self.lne_tsalary.setReadOnly(True)
        self.btn_calc_cf.clicked.connect(self.btn_calc1_clicked)
        self.btn_calc_sal.clicked.connect(self.btn_calc2_clicked)
    def btn_calc1_clicked(self):
        if self.lne_eID.text() != "" and self.lne_day.text() != "" and self.lne_month.text() != "" and self.lne_year.text() != "" and self.cb_mode.currentIndex() != 0:
            index = self.cb_mode.currentText()
            if index == "Walking":
                cf = 0
            elif index == "Cycling":
                cf = 0
            elif index == "Car":
                cf = 3
            elif index == "Motorcycle":
                cf = 1
            elif index == "Auto":
                cf = 4
            elif index == "Bus":
                cf = 0.6
            elif index == "Metro":
                cf = 0
            else:
                w = QtGui.QWidget()
                QtGui.QMessageBox.information(w, "An error occured", "you chose a wrong option")
            eID = self.lne_eID.text()
            day = self.lne_day.text()
            month = self.lne_month.text()
            year = self.lne_year.text()
            cff = cf
            try:
                cursor = self.conn.cursor()
                cursor.execute("INSERT INTO carbon (emp_ID, day, month, year, mode, cf) VALUES (?,?,?,?,?,?)", (eID, day, month, year, index, cff));
                self.conn.commit()
            except sqlite3.Error as e:
                w = QtGui.QWidget()
                QtGui.QMessageBox.information(w, "An error occured", e.args[0])
                return False
            w = QtGui.QWidget()
            QtGui.QMessageBox.information(w, "save succesful", "It has succesfully been saved")
            self.lne_TCF.setText(str(cff))
        else:
            w = QtGui.QWidget()
            QtGui.QMessageBox.information(w, "Error", "Please fill in all the details before calculating")
    def btn_calc2_clicked(self):
        tcf = 0
        month = self.lne_bonuspc_2.text()
        year =  self.lne_bonuspc_3.text()
        ID = self.lne_bonuspc_4.text()
        if month == "":
            w = QtGui.QWidget()
            QtGui.QMessageBox.information(w, "Error", "Please fill in all the details before calculating")
            return False
        cursor = self.conn.cursor()
        cursor.execute("SELECT emp_ID, day, month, year, mode, cf FROM carbon WHERE month = '" + str(month) + "' AND year = '" + str(year) + "' AND emp_ID = '" + str(ID) + "'")
        row = cursor.fetchall()
        for r in row:
            ID, day, month, year, mode, cf = r
            tcf = tcf + cf
        cursor = self.conn.cursor()
        cursor.execute("SELECT salary FROM employee WHERE ID = '" + str(ID) + "'")
        row = cursor.fetchall()
        for r in row:
            sal = r
        if tcf >= 180:
            bonuspp = 0/100
            bonusp = "0%"
        elif tcf >= 140:
            bonuspp = 5/100
            bonusp = "5%"
        elif tcf >= 100:
            bonuspp = 10/100
            bonusp = "10%"
        elif tcf >= 50:
            bonuspp = 20/100
            bonusp = "20%"
        elif tcf > 0:
            bonuspp = 30/100
            bonusp = "30%"
        elif tcf == 0:
            bonuspp = 50/100
            bonusp = "50%"
        sal = sal[0]
        self.lne_bonuspc.setText(bonusp)
        stuff = bonuspp * float(sal)
        self.lne_bonusmon.setText(str(stuff))
        stuff2 = bonuspp * float(sal) + float(sal)
        self.lne_tsalary.setText(str(stuff2))
if __name__=="__main__":
    app=QtGui.QApplication(sys.argv)
    myapp=Ui_Dialog()
    myapp.show()
    sys.exit(app.exec_())
