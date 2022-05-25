#!/usr/bin/python3

import sys
from PySide2 import QtCore, QtWidgets, QtNetwork
from talk import *
from connect import *

class ConnectWindow(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(ConnectWindow, self).__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

class TalkMainWindow(QtWidgets.QMainWindow):        # QtWidgets.QMainWindow 클래스를 상속한 객체 생성, UI 구성.
    def __init__(self, parent=None):
        super(TalkMainWindow, self).__init__(parent)
        self.ui = Ui_TalkWindow()
        self.ui.setupUi(self)
        self.ui.connectButton.clicked.connect(self.connect)     # connectButton 의 clicked 시그널을 connect() 슬롯 함수와 연결.

        self.socket = QtNetwork.QTcpSocket(self)        # QTcpSocket 소켓 객체 생성.
        self.socket.readyRead.connect(self.readData)    # 소켓 객체의 readyReady 시그널을 readData() 함수에서 처리하도록 함.
        self.socket.error.connect(self.displayError)
        self.connectState = False

    def connect(self):      # 접속 대화 상자를 만들고 서버 주소, 퐅, 이름을 입력 받아 서버에 접속 요청.
        if not self.connectState:
            cw = ConnectWindow()
            if cw.exec_() == QtWidgets.QDialog.Accepted:
                self.socket.connectToHost(cw.ui.server.text(), int(cw.ui.port.text()))  # connectToHost 함수를 호출하여 접속 요청한 후, waitForConnected 함수를 호출하여 접속이 허가될 때까지 대기.
                if self.socket.waitForConnected(1000):      # 허가되면 lineEdit 위젯 등으로 입력한 메시지가 서버로 전달되도록 하고, 반대로 서버로부터 오는 메시지는 TextEdit 위젯에 나타내도록 함.
                    self.name = cw.ui.name.text()
                    self.send("login %s" % self.name)
                    self.ui.sendButton.clicked.connect(self.sendClick)
                    self.ui.messageEdit.returnPressed.connect(self.sendClick)
                    self.ui.messageEdit.setFocus()
                    self.ui.connectButton.setText("Disconnect")
                    self.connectState = True
        else:
            self.socket.disconnectFromHost()        # 창을 닫으면 호출됨. 접속 해제.
            self.ui.connectButton.setText("Connect")
            self.connectState = False

    def readData(self):
        message = self.socket.readLine().data().decode("utf-8")
        self.ui.talkMain.append(message)

    def send(self, message):
        self.socket.write(message.encode("utf-8"))

    def sendClick(self):
        self.send("msg %s" % (self.ui.messageEdit.text()))
        self.ui.messageEdit.clear()
        self.ui.messageEdit.setFocus()

    def displayError(self):
        QtWidgets.QMessageBox.information(self, "Connection", "Error during connection")

    def closeEvent(self, event):
        self.socket.disconnectFromHost()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    tmw = TalkMainWindow()
    tmw.show()
    sys.exit(app.exec_())
