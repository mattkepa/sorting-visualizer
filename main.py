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

    is_sorting = False

    run = True
    while run:
        clock.tick(app.FPS)

        draw(app)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type != pygame.KEYDOWN:
                continue

            if event.key == pygame.K_r:
                is_sorting = False
                nums = generate_list(N, MIN_VAL, MAX_VAL)
                app.set_list(nums)
            elif event.key == pygame.K_SPACE and not is_sorting:
                is_sorting = True
            elif event.key == pygame.K_a and not is_sorting:
                app.set_order('ASC')
            elif event.key == pygame.K_d and not is_sorting:
                app.set_order('DESC')
            elif event.key == pygame.K_b and not is_sorting:
                app.set_algorithm('Bubble Sort')
            elif event.key == pygame.K_i and not is_sorting:
                app.set_algorithm('Insertion Sort')
            elif event.key == pygame.K_s and not is_sorting:
                app.set_algorithm('Selection Sort')
            elif event.key == pygame.K_ESCAPE:
                is_sorting = False
                run = False

    pygame.quit()


if __name__ == '__main__':
    main()