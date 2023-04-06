import sys
from ftplib import FTP

host = '192.168.1.103'
port = 21

user = 'TestUser'
passwd = 'qwerty'


def main(cmd, args):
    ftp = FTP()
    ftp.connect(host, port)
    ftp.login(user, passwd)

    if cmd == '--list':
        ftp.retrlines('LIST')
    elif cmd == '--upload':
        input_filename = args[0]
        output_filename = args[1]
        with open(input_filename, 'rb') as input_file:
            ftp.storbinary(f'STOR {output_filename}', input_file)
    elif cmd == '--download':
        input_filename = args[0]
        output_filename = args[1]
        with open(output_filename, 'wb') as output_file:
            ftp.retrbinary(f'RETR {input_filename}', output_file.write)

    ftp.quit()


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2:])
