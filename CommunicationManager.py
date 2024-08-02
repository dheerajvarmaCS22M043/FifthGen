from TCP import TCPDevice
import threading


class CommunicationManager:
    def __init__(self):
        self.devices = {}

    def add_device(self, name: str, ip: str, port: int):
        device = TCPDevice(ip, port)
        self.devices[name] = device

    def communicate(self, name: str, data: str) -> str:
        if name in self.devices:
            device = self.devices[name]
            device.connect()
            device.send(data)
            response = device.receive()
            device.close()
            return response
        else:
            raise ValueError(f"Device {name} not found.")

    def communicate_with_all(self, data: str):
        responses = {}
        threads = []

        def communicate_device(device_name):
            try:
                responses[device_name] = self.communicate(device_name, data)
            except Exception as e:
                responses[device_name] = str(e)

        for name in self.devices:
            thread = threading.Thread(target=communicate_device, args=(name,))
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()

        return responses
