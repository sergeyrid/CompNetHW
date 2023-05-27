import time
import socket
import struct
import random
from datetime import datetime
import sys


def get_checksum(data):
    checksum = 0
    for i in range(0, len(data), 2):
        if i + 1 >= len(data):
            checksum += data[i]
            break
        checksum += (data[i] << 8) + (data[i + 1])
    checksum = (checksum >> 16) + (checksum & 0xffff)
    checksum += checksum >> 16
    return socket.htons(0xffff & ~checksum)


def ping(host):
    client = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.getprotobyname('icmp'))
    client.settimeout(2)

    random_id = random.randint(0, 65535)
    header = struct.pack("bbHHh", 8, 0, 0, random_id, 1)
    payload = str(datetime.now()).encode('utf-8')
    checksum = get_checksum(header + payload)
    header = struct.pack("bbHHh", 8, 0, checksum, random_id, 1)

    packet = header + payload
    while packet:
        sent = client.sendto(packet, (host, 1))
        packet = packet[sent:]
    send_time = time.time()

    data, addr = client.recvfrom(1024)

    checksum = get_checksum(data[20:])
    if checksum != 0:
        raise Exception('Checksum error')

    receive_time = time.time()
    client.close()
    if data is None:
        raise Exception('No response')

    packet_type, code, checksum, packet_id, sequence = struct.unpack("bbHHh", data[20:28])
    if packet_id != random_id:
        raise Exception('Packet ID error')

    ping_time = receive_time - send_time
    return ping_time


def main(argv=None):
    if argv is None:
        argv = sys.argv

    if len(argv) != 2:
        print('Usage: python3 ping.py <host>')
        return

    host = argv[1]

    for _ in range(5):
        try:
            ping_time = ping(host)
            print('Ping time: {0} ms'.format(ping_time * 1000))
        except socket.timeout:
            print('Timeout')
        except Exception as e:
            print(e)

        time.sleep(1)


if __name__ == '__main__':
    main()
