import socket


if __name__ == '__main__':
    socketserver = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    host = socket.gethostname()
    print(host)

    port = 4444

    socketserver.bind(('192.168.1.5', port))

    socketserver.listen(3)

    while True:
        client_socket, address = socketserver.accept()

        print("received connection from %s " % str(address))

        message = "EMRE-hello! Thank you for connecting to the server" + "\r\n"

        encoded_message = message.encode()
        client_socket.send(encoded_message)

        client_socket.close()

