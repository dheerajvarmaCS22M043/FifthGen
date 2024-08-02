import unittest
from unittest.mock import MagicMock
from TCP import TCPDevice
from CommunicationManager import CommunicationManager
from Stub import run_stub_server

class TestTCPDevice(unittest.TestCase):
    def setUp(self):
        self.device = TCPDevice("127.0.0.1", 8000)

    def test_send_receive(self):
        self.device.connect = MagicMock()
        self.device.send = MagicMock()
        self.device.receive = MagicMock(return_value="ACK")
        self.device.close = MagicMock()

        self.device.connect()
        self.device.send("Hello")
        response = self.device.receive()
        self.device.close()

        self.device.connect.assert_called_once()
        self.device.send.assert_called_once_with("Hello")
        self.device.receive.assert_called_once()
        self.device.close.assert_called_once()
        self.assertEqual(response, "ACK")

class TestCommunicationManager(unittest.TestCase):
    def setUp(self):
        self.manager = CommunicationManager()
        self.manager.add_device("device1", "127.0.0.1", 8000)

    def test_communicate_with_device(self):
        self.manager.devices["device1"].connect = MagicMock()
        self.manager.devices["device1"].send = MagicMock()
        self.manager.devices["device1"].receive = MagicMock(return_value="ACK")
        self.manager.devices["device1"].close = MagicMock()

        response = self.manager.communicate("device1", "Hello")

        self.manager.devices["device1"].connect.assert_called_once()
        self.manager.devices["device1"].send.assert_called_once_with("Hello")
        self.manager.devices["device1"].receive.assert_called_once()
        self.manager.devices["device1"].close.assert_called_once()
        self.assertEqual(response, "ACK")

if __name__ == "__main__":
    unittest.main()

# if __name__ == "__main__":
#     run_stub_server("127.0.0.1", 8000)
