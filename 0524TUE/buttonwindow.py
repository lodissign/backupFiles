import sys
from tkinter import Button
from PySide2 import QtCore, QtWidgets

class ButtonWindow(QtWidgets.QWidget):
 def __init__(self, msg):
  QtWidgets.QWidget.__init__(self)
  self.setWindowTitle("Button Window")
  self.setGeometry(300, 200, 200, 200)
  self.button = QtWidgets.QPushButton(msg, self)
  self.button.setGeometry(50, 30, 70, 30)

QtCore.QObject.connect( Button, QtCore.SIGNAL('clicked()'), QtCore.SLOT('hello()'))
self.button.clicked.connect(self.hello)
def hello(self):
 print('Hello World')