import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

data = "Hello Server"
print("Send '{}' to Server.".format(data))

sock.sendto("Hello".encode(),('127.0.0.1',1234))
data, addr = sock.recvfrom(512)

print("Received '{}' from Server({}).".format(data.decode(), addr))
