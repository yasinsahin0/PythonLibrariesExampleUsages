import socket

host_port = ("127.0.0.1", 12000)

def server_udp(addr):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind(addr)
    while True:
        message, address = server_socket.recvfrom(1024)
        message = message.upper()
        print("Server UDP message : ",message)


def server_tcp(addr):

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(addr)
    server_socket.listen()
    conn, addr = server_socket.accept()
    with conn:
        print(f"Connected by {addr}")
        while True:
            data = conn.recv(1024)
            print("Server TCP message : ",data)
            if not data:
                break
            conn.sendall(data)

if __name__ == "__main__":
    server_tcp(host_port)