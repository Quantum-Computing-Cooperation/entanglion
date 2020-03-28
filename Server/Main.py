import socket
from threading import Thread

import Game


class GameThread(Thread):
    def __init__(self, socket_one, socket_two):
        Thread.__init__(self)
        self.game = Game(socket_one, socket_two)

    def run(self):
        self.game.run()


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
