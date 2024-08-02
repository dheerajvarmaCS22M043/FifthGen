# FifthGen
## Overview
This project implements a real-time communication system for managing multiple devices in a manufacturing plant. The system supports TCP/IP communication, handles multiple devices simultaneously, and is designed to be extensible for future communication protocols.

## Features
* TCP/IP Communication: Connects, reads, and writes data to devices using TCP/IP.
* Simultaneous Communication: Communicates with multiple devices concurrently.
* Extensible Protocols: Supports future additions of communication protocols.
* Testing: Includes a stub server for testing TCP/IP communication and unit tests for code validation.

## Files
* TCP.py: Defines the TCPDevice class for handling TCP/IP communication.
* CommunicationManager.py: Manages multiple devices and facilitates communication with them.
* Protocol.py: Provides an abstract base class for communication protocols and a concrete implementation for TCP.
* Stub.py: Implements a stub server for simulating device behavior for testing purposes.
* UnitTest.py: Contains unit tests for validating the functionality of the TCPDevice and CommunicationManager classes.

## Installation
To set up the project, clone the repository and ensure you have Python 3 installed.
* git clone https://github.com/yourusername/your-repository.git 
* cd your-repository

* code execution starts from UnitTest.py file

## Usage

* from CommunicationManager import CommunicationManager

### Initialize the communication manager
* manager = CommunicationManager()

### Add a device
* manager.add_device("device1", "127.0.0.1", 8000)

### Communicate with a device
* response = manager.communicate("device1", "Hello, device!")
* print(response)  # Should print "ACK" if the stub server is running

