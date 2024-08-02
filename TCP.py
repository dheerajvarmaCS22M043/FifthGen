import socket
import threading
from typing import Dict, Callable

class TCPDevice:
    def __init__(self, ip: str, port: int):
        self.ip = ip
        self.port = port
        self.socket = None

    def connect(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((self.ip, self.port))

    def send(self, data: str):
        self.socket.sendall(data.encode())

    def receive(self, buffer_size: int = 1024) -> str:
        return self.socket.recv(buffer_size).decode()

    def close(self):
        if self.socket:
            self.socket.close()
