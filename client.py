
import socket

HOST = "127.0.0.1"
PORT = 50000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((HOST, PORT))

message = "send time"

client.sendall(message.encode("utf-8"))

response = client.recv(1024).decode("utf-8")

print("Antwort vom Server:", response)

client.close()