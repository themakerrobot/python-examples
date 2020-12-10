import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('127.0.0.1', 1234))

data, addr = sock.recvfrom(512)
print("Received '{}' from Client({}).".format(data.decode(), addr))

data = "Hello Client"
print("Send '{}' to Client.".format(data))
sock.sendto(data.encode(), addr)
