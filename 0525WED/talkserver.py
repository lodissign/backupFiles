#!/usr/bin/python3

import random
from PySide2 import QtCore, QtNetwork

class Server(QtNetwork.QTcpServer):     # QtNetwork.QTcpServer 를 상속받는 Server class 객체 생성.
    def __init__(self, parent=None):    # 생성자
        super(Server, self).__init__(parent)
        self.newConnection.connect(self.newClient)      # 클라이언트로 부터 새로운 연결 요청이 왔을 때 발생하는 newConnection 시그널을 newClient()라는 슬롯 함수에 연결하여 새로운 연결 처리.

        self.clients = {}

    def newClient(self):        # 
        socket = self.nextPendingConnection()       # 클라이언트와 연결된 소켓(떨어져 있는 두 호스트를 연결해주는 도구로써 인터페이스 역할) 획득.
        socket.readyRead.connect(self.readData)     # 소켓이 데이터를 수신할 때 발생하는 readyRead 시그널은 readData() 함수와 연동.
        socket.disconnected.connect(self.disconnectClient)  # 연결이 끊어질 때 발생하는 disconnected 시그널은 disconnecClient() 함수에서 처리하도록 함.
        self.clients[socket] = {}
        self.clients[socket]["name"] = u"손님-%d" % random.randint(1, 100)

    def disconnectClient(self):     # 사전을 확인해 해당하는 클라이언트를 제거, 등록된 모든 클라이언트에게 해당 클라이언트가 접속을 끝내고 나갔다는 메시지 방송.
        socket = self.sender()
        self.sendAll(u"<em>%s 님이 나가셨습니다.</em>" % self.clients[socket]["name"])
        self.clients.pop(socket)

    def readData(self):     # 수신 데이터를 처리하여 클라이언트가 접속을 요청하는 메시지이면 클라이언트의 이름을 사전에 등록, 채팅 메시지이면 등록된 모든 클라이언트한테 메시지를 방송.
        socket = self.sender()
        line = socket.readLine().data().decode("utf-8")
        cmd, value = line.split(" ", 1)
        if cmd == "login":
            if self.Exist(value):
                name = self.clients[socket]["name"]
                self.send(socket, u"<em>이름이 이미 존재합니다. 자동으로 설정합니다...</em>")
            else:
                name = value
                self.clients[socket]["name"] = name
            self.sendAll(u"<em>%s 님이 들어왔습니다.</em>" % name)
        elif cmd == "msg":
            message = "<%s> : %s" % (self.clients[socket]["name"], value)
            self.sendAll(message)

    def send(self, socket, message):
        socket.write(message.encode("utf-8"))

    def sendAll(self, message):
        for c in self.clients:
            self.send(c, message)

    def Exist(self, name):
        for c in self.clients:
            if name == self.clients[c]["name"]:
                return True

if __name__ == '__main__':

    import sys, signal
    signal.signal(signal.SIGINT, signal.SIG_DFL)    # 
    app = QtCore.QCoreApplication(sys.argv)
    #QtCore.QTextCodec.setCodecForTr(QtCore.QTextCodec.codecForName("eucKR"))
    serv = Server()
    port = 8080
    serv.listen(port=port)      # 8080 포트로 클라이언트가 접속하길 기다림.
    print("The server is running with port %d" % port)      # port 번호(8080) 출력.
    sys.exit(app.exec_())
