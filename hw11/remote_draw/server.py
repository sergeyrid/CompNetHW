import socket
import pygame


def main():
    pygame.init()

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('localhost', 8000))
    s.listen()

    conn, addr = s.accept()

    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("Server")

    exit_flag = False
    while not exit_flag:
        message = conn.recv(1024).decode()
        mouse_event = message.split()

        if mouse_event[0] == 'MOUSE_MOVE':
            pygame.draw.circle(screen, (0, 0, 255), (int(mouse_event[1]), int(mouse_event[2])), 10)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_flag = True

    s.close()


if __name__ == '__main__':
    main()
