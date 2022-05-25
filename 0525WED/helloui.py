import sys
from PySide2 import QtCore, QtWidgets
from hello import *

class controlMainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(controlMainWindow, self).__init__(parent)
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)

if __name__=="__main__":
    app=QtWidgets.QApplication(sys.argv)
    mySW=controlMainWindow()
    mySW.show()
    sys.exit(app.exec_())