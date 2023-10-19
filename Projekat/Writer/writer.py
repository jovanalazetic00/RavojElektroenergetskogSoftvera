import socket
from ClientUI import ClientUI


class Client:

    def __init__(self):
        self.port = 8000
        self.server = socket.gethostbyname(socket.gethostname())
        self.address = (self.server, self.port)
        self.format = 'utf-8'

        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect(self.address)
        self.connected = True
        self.menu = ClientUI()

    def send_message(self, message):
        self.sock.send(message.encode(self.format))

    def client_UI(self):
        while self.connected:
            self.menu.Options()
            _input = input()
            self.connected = self.menu.Handle(_input, self.send_message)


def main():
    client = Client()
    client.client_UI()


if __name__ == "__main__":
    main()
