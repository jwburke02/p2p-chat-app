import socket
from threading import Thread
import Discovery

def messageListening():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(('', 0))
        print(f"Listening for messages on port: {s.getsockname()[1]}")
        Discovery.updatePort(s.getsockname()[1])
        s.listen()
        while True:
            conn, addr = s.accept()
            with conn:
                while True:
                    data = conn.recv(1024)
                    if not data:
                        break
                    print(f"Received message: {data.decode()}")

def createListener():
    listener = Thread(target=messageListening)
    listener.daemon = True
    listener.start()

def sendMessage(HOST, PORT, MESSAGE):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(MESSAGE.encode())
        