import pygame
import random


def generate_list(n, min_val, max_val):
    """
    Generates a list of numbers of a given length in a given interval and returns the result
    :param n: int - lenght of list
    :param min_val: int - min value in interval
    :param max_val: int - max value in interval
    """
    array = []
    for _ in range(n):
        val = random.randint(min_val, max_val)
        array.append(val)
    return array


def draw(app):
    """
    Clears the entire screen and redraws everything on it
    :param: app: AppInfo - app object with configuration and informations
    """
    app.window.fill(app.BACKGROUND_COLOR)
    draw_list(app)
    pygame.display.update()


def draw_list(app):
    """
    Draws rectangle for every number in list
    :param: app: AppInfo - app object with configuration and informations
    """
    array = app.list

    for i, val in enumerate(array):
        color = app.GRAYSCALE[i % 3]
        bar_width = app.block_width
        bar_height = (val - app.min_val) * app.block_height  # -> 0 height for min value
        x = app.start_x + i * bar_width
        y = app.height - bar_height
        pygame.draw.rect(app.window, color, (x, y, bar_width, bar_height))
