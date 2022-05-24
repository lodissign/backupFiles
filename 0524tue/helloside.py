#!/usr/bin/python3
import sys
from PySide2 import QtCore, QtWidgets

app = QtWidgets.QApplication(sys.argv)
# label = QtWidgets.QLabel("Hello World")
label = QtWidgets.QLabel("<font>Hello World</font>")
label.show()
app.exec_()
sys.exit()