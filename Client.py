import socket
from Message import Message

class Client:
    def __init__(self, client_address):
        self.client_address = client_address

    def _start_socket(self):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect(self.client_address)

    def _close_socket(self):
        self.client_socket.close()

    def PushToServer(self, fm, sm):
        self._start_socket()
        Message(self.client_socket).PushMessage(fm, sm)

    def ReceiveFromServer(self):
        mess = Message(self.client_socket).LoadMessage()
        self._close_socket()
        return mess

