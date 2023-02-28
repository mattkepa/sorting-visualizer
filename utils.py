import pygame
import os
import random


CONTROLS = {
    'KEY_R': pygame.image.load(os.path.join('assets', 'img', 'key_icon_R.png')),
    'KEY_SPACE': pygame.image.load(os.path.join('assets', 'img', 'key_icon_SPACE.png')),
    'KEY_A': pygame.image.load(os.path.join('assets', 'img', 'key_icon_A.png')),
    'KEY_D': pygame.image.load(os.path.join('assets', 'img', 'key_icon_D.png')),
    'KEY_B': pygame.image.load(os.path.join('assets', 'img', 'key_icon_B.png')),
    'KEY_I': pygame.image.load(os.path.join('assets', 'img', 'key_icon_I.png')),
    'KEY_S': pygame.image.load(os.path.join('assets', 'img', 'key_icon_S.png'))
}


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
    title = app.FONT_TITLE.render(f'{app.algo_name} - {"Ascedinding" if app.sort_order == "ASC" else "Descending"}', True, app.COLORS['black'])
    app.window.blit(title, (app.width // 2 - title.get_width() // 2, 50))
    draw_controls(app)
    draw_list(app)
    pygame.display.update()


def draw_controls(app):
    """
    Draws menu with key images and text to control program flow
    :param: app: AppInfo - app object with configuration and informations
    """
    # Control - Reset list
    app.window.blit(CONTROLS['KEY_R'], (50, 125))
    control_text = app.FONT_CONTROLS.render('Reset', True, app.COLORS['gray'])
    app.window.blit(control_text, (105, 125 + 20 - control_text.get_height() // 2))
    # Control - Start Sorting
    app.window.blit(CONTROLS['KEY_SPACE'], (225, 125))
    control_text = app.FONT_CONTROLS.render('Start Sorting', True, app.COLORS['gray'])
    app.window.blit(control_text, (320, 125 + 20 - control_text.get_height() // 2))
    # Control - Set Ascending order
    app.window.blit(CONTROLS['KEY_A'], (585, 125))
    control_text = app.FONT_CONTROLS.render('Ascending', True, app.COLORS['gray'])
    app.window.blit(control_text, (640, 125 + 20 - control_text.get_height() // 2))
    # Control - Set Descenting order
    app.window.blit(CONTROLS['KEY_D'], (775, 125))
    control_text = app.FONT_CONTROLS.render('Descending', True, app.COLORS['gray'])
    app.window.blit(control_text, (830, 125 + 20 - control_text.get_height() // 2))
    # Control - Set Bubble Sort Algorithm
    app.window.blit(CONTROLS['KEY_B'], (50, 185))
    control_text = app.FONT_CONTROLS.render('Bubble Sort', True, app.COLORS['gray'])
    app.window.blit(control_text, (105, 185 + 20 - control_text.get_height() // 2))
    # Control - Set Insertion Sort Algorithm
    app.window.blit(CONTROLS['KEY_I'], (350, 185))
    control_text = app.FONT_CONTROLS.render('Insertion Sort', True, app.COLORS['gray'])
    app.window.blit(control_text, (405, 185 + 20 - control_text.get_height() // 2))
    # Control - Set Selection Sort Algorithm
    app.window.blit(CONTROLS['KEY_S'], (650, 185))
    control_text = app.FONT_CONTROLS.render('Selection Sort', True, app.COLORS['gray'])
    app.window.blit(control_text, (705, 185 + 20 - control_text.get_height() // 2))



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
