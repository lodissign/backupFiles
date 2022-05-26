#!/usr/bin/python3
import sys
from PySide2 import QtCore, QtWidgets

# class LayoutWindow(QtWidgets.QWidget):
#     def __init__(self):
#         QtWidgets.QWidget.__init__(self)
#         # self.setWindowTitle("Layout Window")
#         vbox=QtWidgets.QVBoxLayout(self)
#         hbox1=QtWidgets.QHBoxLayout()
#         hbox2=QtWidgets.QHBoxLayout()
#         hbox3=QtWidgets.QHBoxLayout()

#         self.one=QtWidgets.QPushButton("One", self)
#         self.two=QtWidgets.QPushButton("Two", self)
#         self.three=QtWidgets.QPushButton("Three", self)
#         self.four=QtWidgets.QPushButton("Four", self)
#         self.five=QtWidgets.QPushButton("Five", self)

#         vbox.addWidget(hbox1)
#         vbox.addWidget(hbox2)
#         vbox.addWidget(hbox3)

#         hbox1.addWidget()

class QGridLayout(QtWidgets.QGridLayout):
    def __init__(self):
        QtWidgets.QGridLayout.__init__(self)

        self.one=QtWidgets.QPushButton("One", self)
        self.two=QtWidgets.QPushButton("Two", self)
        self.three=QtWidgets.QPushButton("Three", self)
        self.four=QtWidgets.QPushButton("Four", self)
        self.five=QtWidgets.QPushButton("Five", self)

        hbox1=QtWidgets.QGridLayout()
        hbox2=QtWidgets.QGridLayout()
        hbox3=QtWidgets.QGridLayout()

        hbox1.addWidget(self.one)
