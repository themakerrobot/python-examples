import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 3333))
data = "Hello Server"
print("Send '{}' to Server.".format(data))
client.send(data.encode())

data = client.recv(512)
print("Received '{}' from Server.".format(data.decode()))
