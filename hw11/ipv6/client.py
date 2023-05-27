import socket


def main():
    client_socket = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
    client_socket.connect(('::', 8080))

    data = "Hello, world!"
    client_socket.sendall(data.encode('utf-8'))

    response = client_socket.recv(1024)
    print(response.decode('utf-8'))


if __name__ == "__main__":
    main()
