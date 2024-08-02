import socket

def run_stub_server(ip: str, port: int):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((ip, port))
    server_socket.listen(1)
    print(f"Stub server running on {ip}:{port}")

    while True:
        client_socket, addr = server_socket.accept()
        print(f"Connection from {addr}")
        data = client_socket.recv(1024)
        print(f"Received: {data.decode()}")
        client_socket.sendall(b"ACK")
        client_socket.close()
