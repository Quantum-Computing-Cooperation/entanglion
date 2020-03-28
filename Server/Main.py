import socket
from threading import Thread


class GameThread(Thread):
    def __init__(self, socket_one, socket_two):
        Thread.__init__(self)
        # Creates a game, initializes everything
        self.socket_blue = socket_one
        self.socket_red = socket_two

    def run(self):
        # Runs the game, ensures smooth exit so as to not crash the server
        # below is just a prototype of communication

        print("Connection from : ", clientAddress)
        # self.csocket.send(bytes("Hi, This is from Server..",'utf-8'))
        msg = ''
        while True:
            data = self.csocket.recv(2048)
            msg = data.decode()
            if msg == 'bye':
                break
            print("from client", msg)
            self.csocket.send(bytes(msg, 'UTF-8'))
        print("Client at ", clientAddress, " disconnected...")


HOST = "127.0.0.1"
PORT = 5210
pending_connections = {}

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.bind((HOST, PORT))
    print("Server started !")
    print("Waiting for client request ...")
    while True:
        server.listen(1)
        client, clientAddr = server.accept()
        if clientAddr in pending_connections:
            newGame = GameThread(pending_connections[clientAddr], client)
            del pending_connections[clientAddr]
            newGame.start()
        else:
            client.sendall(bytes("Partner's IP", 'UTF-8'))
            partner_ip = client.recv(1024).decode('UTF-8')
            pending_connections[partner_ip] = client
