import pygame
from app_info import AppInfo
from utils import generate_list, draw, bubble_sort, insertion_sort, selection_sort


pygame.init()


def main():
    clock = pygame.time.Clock()
    # Settings for numbers list
    MIN_VAL = 0
    MAX_VAL = 100
    N = 75
    #####

    app = AppInfo(1000, 800, generate_list(N, MIN_VAL, MAX_VAL), 'Bubble Sort', bubble_sort)

    algo_generator = None
    sorting = False

    run = True
    while run:
        clock.tick(app.FPS)

        if sorting:
            try:
                next(algo_generator)
            except StopIteration:
                sorting = False
        else:
            draw(app)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type != pygame.KEYDOWN:
                continue

            if event.key == pygame.K_r:
                sorting = False
                nums = generate_list(N, MIN_VAL, MAX_VAL)
                app.set_list(nums)
            elif event.key == pygame.K_SPACE and not sorting:
                sort_algo = app.algorithm
                algo_generator = sort_algo(app)
                sorting = True
            elif event.key == pygame.K_a and not sorting:
                app.set_order('ASC')
            elif event.key == pygame.K_d and not sorting:
                app.set_order('DESC')
            elif event.key == pygame.K_b and not sorting:
                app.set_algorithm('Bubble Sort', bubble_sort)
            elif event.key == pygame.K_i and not sorting:
                app.set_algorithm('Insertion Sort', insertion_sort)
            elif event.key == pygame.K_s and not sorting:
                app.set_algorithm('Selection Sort', selection_sort)
            elif event.key == pygame.K_ESCAPE:
                sorting = False
                run = False

    pygame.quit()


if __name__ == '__main__':
    main()