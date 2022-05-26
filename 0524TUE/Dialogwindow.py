import sys
from PySide2 import QtCore, QtWidgets


class DialogWindow(QtWidgets.QDialog):
 def __init__(self):
  QtWidgets.QDialog.__init__(self)
  self.setWindowTitle("Dialog Window")
  vbox = QtWidgets.QVBoxLayout(self)
  hbox1 = QtWidgets.QHBoxLayout()
  hbox2 = QtWidgets.QHBoxLayout()
  self.ok = QtWidgets.QPushButton("OK", self)
  self.cancel = QtWidgets.QPushButton("Cancel", self)
  vbox.addLayout(hbox1)
  vbox.addLayout(hbox2)
  hbox1.addWidget(QtWidgets.QLabel("Enter your name", self))
  self.lineedit = QtWidgets.QLineEdit(self)
  hbox1.addWidget(self.lineedit)
  hbox2.addWidget(self.ok)
  hbox2.addWidget(self.cancel)
  
  self.ok.clicked.connect(self.accept)
  self.cancel.clicked.connect(self.reject)
 
if __name__ == "__main__":
 app = QtWidgets.QApplication(sys.argv)
 dg = DialogWindow()
 result = dg.exec_()
 if result == QtWidgets.QDialog.Accepted:
  print("Your name is", dg.lineedit.text())
 elif result == QtWidgets.QDialog.Rejected:
  print("Input canceled")
