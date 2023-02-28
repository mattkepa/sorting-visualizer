import pygame


pygame.init()


def main():
    clock = pygame.time.Clock()
    window = pygame.display.set_mode((1000, 800))

    run = True
    while run:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

    pygame.quit()


if __name__ == '__main__':
    main()