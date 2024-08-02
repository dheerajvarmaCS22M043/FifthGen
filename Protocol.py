class Protocol:
    def send(self, device, data: str):
        pass

    def receive(self, device) -> str:
        pass

class TCPProtocol(Protocol):
    def send(self, device, data: str):
        device.send(data)

    def receive(self, device) -> str:
        return device.receive()
