import sys
from PyQt5.QtWidgets import QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from ClinicManagmentSystemUI import Ui_Dialog

class MainWindow:
    def __init__(self):
        self.main_win=QMainWindow()
        self.ui=Ui_Dialog()
        self.ui.setupUi(self.main_win)


    def show(self):
        self.main_win.show()




if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main_win=QMainWindow()
    main_win.show()
    sys.exit(app.exec_())
