import sys
from PySide2 import QtCore, QtWidgets


class DialogWindow(QtWidgets.QDialog):  # QtWidgets.QDialog를 상속받음.
 def __init__(self):
  QtWidgets.QDialog.__init__(self)
  self.setWindowTitle("Dialog Window")  # 대화 상자 맨 위의 window title을 Dialog Window로 설정.
  vbox = QtWidgets.QVBoxLayout(self)  # vertical 1개
  hbox1 = QtWidgets.QHBoxLayout()
  hbox2 = QtWidgets.QHBoxLayout()   # horizontal 2개
  self.ok = QtWidgets.QPushButton("OK", self)   # OK push button
  self.cancel = QtWidgets.QPushButton("Cancel", self)   # Cancel push button
  
  vbox.addLayout(hbox1)
  vbox.addLayout(hbox2)   # vertical 2개.
  
  hbox1.addWidget(QtWidgets.QLabel("Enter your name", self))    # addWidget으로 1번째 horizontal 줄에 Qlabel 넣음.
  self.lineedit = QtWidgets.QLineEdit(self)   
  hbox1.addWidget(self.lineedit)    # QLineEdit 넣음.
  hbox2.addWidget(self.ok)    # 2번째 horizontal 줄에 self.ok 에 저장돼있던 OK push button 넣음. 
  hbox2.addWidget(self.cancel)
  
  self.ok.clicked.connect(self.accept)    # OK button 클릭 시, accept
  self.cancel.clicked.connect(self.reject)
 
if __name__ == "__main__":
 app = QtWidgets.QApplication(sys.argv)
 dg = DialogWindow()
 result = dg.exec_()
 if result == QtWidgets.QDialog.Accepted:
  print("Your name is", dg.lineedit.text())
 elif result == QtWidgets.QDialog.Rejected:
  print("Input canceled")
