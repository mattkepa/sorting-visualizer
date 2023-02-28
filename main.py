import pygame
from app_info import AppInfo
from utils import generate_list, draw


pygame.init()


def main():
    clock = pygame.time.Clock()
    # Settings for numbers list
    MIN_VAL = 0
    MAX_VAL = 100
    N = 75
    #####

    app = AppInfo(1000, 800, generate_list(N, MIN_VAL, MAX_VAL))

    run = True
    while run:
        clock.tick(app.FPS)

        draw(app)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

    pygame.quit()


if __name__ == '__main__':
    main()