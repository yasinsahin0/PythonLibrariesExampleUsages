import time
import socket

UDP = socket.SOCK_DGRAM # UDP protokolüdür
TCP = socket.SOCK_STREAM # TCP Protokolüdür.
RAW = socket.SOCK_RAW # Ham veri protokolüdür.
c = socket.SOCK_RDM
d = socket.SOCK_SEQPACKET

host_port = ("127.0.0.1", 12000)
message = b'test'

print("Local - Message type : ",type(message))
print("Local - Message : ",message)
# client_socket.settimeout(1.0)
def client_udp(addr):
    client_socket = socket.socket(socket.AF_INET, UDP)
    client_socket.sendto(message, addr)
    client_socket.close()

def client_tcp(addr):
    with socket.socket(socket.AF_INET, TCP) as s:
        s.connect(addr)
        s.sendall(message)
        data = s.recv(1024)
    print("Client TCP message : ",data)

if __name__ == "__main__":
    client_tcp(host_port)