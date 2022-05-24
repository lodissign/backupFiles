#!/usr/bin/python3
import sys
from PySide2 import QtCore, QtGui, QtWidgets


class EventWindow(QtWidgets.QWidget):
 def __init__(self):
  QtWidgets.QWidget.__init__(self)
  self.setWindowTitle("Event Window")
  self.setGeometry(300, 300, 300, 300)
 
 def keyPressEvent(self, event):
  if event.key() == QtCore.Qt.Key_Escape:
   self.close()
 
 def mouseDoubleClickEvent(self, event):
  self.close()
 points = []
 
 def mouseMoveEvent(self, event):
  print("x=", event.x(), ", y=", event.y())
  self.points.append((event.x(), event.y()))
  self.update()
 
 def paintEvent(self, event):
  painter = QtGui.QPainter()
  painter.begin(self)
  painter.setPen(QtGui.QPen(QtCore.Qt.red, 10, QtCore.Qt.SolidLine, QtCore.Qt.RoundCap))
 
  for p in self.points:
   painter.drawPoint(p[0], p[1])
 
  painter.end()


if __name__ == "__main__":
 app = QtWidgets.QApplication(sys.argv)
 ew = EventWindow()
 ew.show()
 sys.exit(app.exec_())
