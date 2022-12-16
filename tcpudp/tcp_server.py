import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 3333))
server.listen(1)

client, addr = server.accept()
data = client.recv(512)
print("Received '{}' from Client({}).".format(data.decode(), addr))
 
data = "Hello Client"
print("Send '{}' to Client.".format(data))
client.send(data.encode())
client.close()
server.close()
