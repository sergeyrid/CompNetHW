import socket
import pygame


def main():
    pygame.init()

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('localhost', 8000))

    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("Client")

    exit_flag = False
    while not exit_flag:
        mouse_pos = pygame.mouse.get_pos()
        s.sendall(f'MOUSE_MOVE {mouse_pos[0]} {mouse_pos[1]} '.encode())

        pygame.draw.circle(screen, (0, 0, 255), (mouse_pos[0], mouse_pos[1]), 10)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_flag = True

    s.close()


if __name__ == '__main__':
    main()
