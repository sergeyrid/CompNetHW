import socket


def handle_client(client_socket):
    data = client_socket.recv(1024).decode('utf-8')
    upper_case_data = data.upper()
    print(data, '->', upper_case_data)
    client_socket.sendall(upper_case_data.encode('utf-8'))


def main():
    server_socket = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
    server_socket.bind(('::', 8080))
    server_socket.listen(1)

    while True:
        client_socket, address = server_socket.accept()
        handle_client(client_socket)


if __name__ == '__main__':
    main()
