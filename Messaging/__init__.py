import socket
from threading import Thread
import Discovery
import Database
import Utils

def messageListening():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(('', 0))
        Discovery.updatePort(s.getsockname()[1])
        s.listen()
        while True:
            conn, addr = s.accept()
            with conn:
                while True:
                    data = conn.recv(1024)
                    if not data:
                        break
                    received_message = data.decode()
                    user = Utils.getUserFromAddress(addr)
                    if not Database.isHostBlocked(addr[0]):
                        if Database.hostExistsInCollection(addr[0], user):
                            Database.addMessageToHostDoc(addr[0], user, received_message, False)
                        else:
                            Database.createHostDoc(addr[0], user, received_message, False)

def createListener():
    listener = Thread(target=messageListening)
    listener.daemon = True
    listener.start()

def sendMessage(HOST, PORT, MESSAGE, USER):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(MESSAGE.encode())
        if Database.hostExistsInCollection(HOST, USER):
            Database.addMessageToHostDoc(HOST, USER, MESSAGE, True)
        else:
            Database.createHostDoc(HOST, USER, MESSAGE, True)
        