# FifthGen
TCP.py:

Defines the TCPDevice class, which handles the TCP/IP communication with individual devices.
This class provides methods to connect, send data, receive data, and close the connection.
CommunicationManager.py:

Defines the CommunicationManager class, which manages multiple devices and facilitates communication with them.
This class can add devices, send data to a specific device, or communicate with all devices simultaneously using threading.
It abstracts the communication process, allowing the use of different protocols.
Protocol.py:

Defines a base Protocol class and a TCPProtocol class that extends it.
The base class provides a common interface for different communication protocols.
The TCPProtocol class implements this interface specifically for TCP communication.
Stub.py:

Defines a stub server that simulates a real device or server for testing purposes.
It listens for TCP connections, receives data, and responds with a simple "ACK" message.
This stub can be used to test your communication system without needing actual devices.
UnitTest.py:

Contains unit tests for the TCPDevice and CommunicationManager classes.
The tests use Python’s unittest framework and the unittest.mock library to simulate device behavior and verify the functionality of the communication methods.
This file ensures that the components of your system work as expected.
