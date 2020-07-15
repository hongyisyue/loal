import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 93))
s.listen(5)

while True:
    clientsocket, address = s.accept()
    print("Connection from {address} has been established")
    clientsocket.send(bytes("testtesttest", "utf-8"))
    clientsocket.close()