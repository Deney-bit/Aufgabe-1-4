
import socket
from datetime import datetime

HOST = "127.0.0.1"
PORT = 50000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

print("Server started. Waiting for requests...")

while True:
    connection, address = server.accept()

    with connection:
        print("Client connected:", address)

        request = connection.recv(1024).decode("utf-8")

        if request == "send time":
            current_time = datetime.now().strftime(
                "%d.%m.%Y %H:%M:%S"
            )
            response = current_time
        else:
            response = "Unknown request"

        connection.sendall(response.encode("utf-8"))

        print("Response sent:", response)