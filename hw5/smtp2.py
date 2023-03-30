from socket import *
from email.message import EmailMessage
import sys

sender = 'sender@mail.ru'
host = 'mail.spbu.ru'
port = 25
recv_len = 1024


def main(receiver, text):
    client_socket = socket(AF_INET, SOCK_STREAM)

    client_socket.connect((host, port))
    recv = client_socket.recv(recv_len)
    if recv.decode()[:3] != '220':
        print('Connection to server failed', file=sys.stderr)
        return

    client_socket.send('EHLO\r\n'.encode())
    recv = client_socket.recv(recv_len)
    if recv.decode()[:3] != '250':
        print('EHLO command failed', file=sys.stderr)
        return

    client_socket.send(f'MAIL FROM:{sender}\r\n'.encode())
    recv = client_socket.recv(recv_len)
    if recv.decode()[:3] != '250':
        print('Sender not accepted', file=sys.stderr)
        return

    client_socket.send(f'RCPT TO:{receiver}\r\n'.encode())
    recv = client_socket.recv(recv_len)
    if recv.decode()[:3] != '250':
        print('Sender not accepted', file=sys.stderr)
        return

    client_socket.send('DATA\r\n'.encode())
    recv = client_socket.recv(recv_len)
    if recv.decode()[:3] != '354':
        print('DATA command failed', file=sys.stderr)
        return

    msg = EmailMessage()
    msg['Subject'] = ''
    msg['From'] = sender
    msg['To'] = receiver
    msg.set_content(text)
    msg_str = msg.as_string()
    client_socket.send(f'{msg_str}.\r\n'.encode())
    recv = client_socket.recv(recv_len)
    if recv.decode()[:3] != '250':
        print('Message not accepted', file=sys.stderr)
        return

    client_socket.send('QUIT\r\n'.encode())
    recv = client_socket.recv(recv_len)
    if recv.decode()[:3] != '221':
        print('Failed to close connection', file=sys.stderr)
        return


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print('Specify a receiver and a message to send', file=sys.stderr)
    else:
        main(sys.argv[1], sys.argv[2])
