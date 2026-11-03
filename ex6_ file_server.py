import socket

def file_transfer_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 12345))
    server_socket.listen(1)

    print("Server listening on port 12345...")

    connection, address = server_socket.accept()
    print("Connected by", address)

    filename = connection.recv(1024).decode()
    print("Receiving file:", filename)

    with open("received_" + filename, 'wb') as file:
        while True:
            data = connection.recv(1024)
            if not data:
                break
            file.write(data)

    print("File received successfully")

    connection.close()
    server_socket.close()

if __name__ == "__main__":
    file_transfer_server()
