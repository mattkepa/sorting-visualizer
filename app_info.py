import pygame
import os
import math


pygame.font.init()


class AppInfo:
    """
    Configuration of app's information and constants

    Init params:
    :param width: int - width of program's window in pixels
    :param height: int - height of program's window in pixels
    :param arr: list[int] - list of numbers
    :param algo_name: str - name of sorting algorithm function to display
    :param algo_fn: function - sorting function
    """

    # CONSTANTS
    COLORS = {
        'white': (255, 255, 255),
        'black': (34, 34, 34),
        'gray': (142, 142, 147),
        'gray1': (174, 174, 178),
        'gray2': (199, 199, 204),
        'gray3': (209, 209, 214),
        'red': (255, 59, 48),
        'green': (52, 199, 89),
    }
    BACKGROUND_COLOR = COLORS['white']
    GRAYSCALE = [COLORS['gray1'], COLORS['gray2'], COLORS['gray3']]
    SIDE_PADDING = 100
    TOP_PADDING = 275
    FPS = 60
    FONT_TITLE = pygame.font.Font(os.path.join(os.path.dirname(__file__), 'assets', 'fonts', 'CircularStd-Medium.ttf'), 30)
    FONT_CONTROLS = pygame.font.Font(os.path.join(os.path.dirname(__file__), 'assets', 'fonts', 'CircularStd-Book.ttf'), 18)


    def __init__(self, width, height, arr, algo_name, algo_fn):
        self.width = width
        self.height = height
        self.window = pygame.display.set_mode((width, height))
        pygame.display.set_caption('Sorting Algorithms Visualizer')
        self.algorithm = algo_fn
        self.algo_name = algo_name
        self.sort_order = 'ASC'
        self.set_list(arr)

    def set_list(self, arr):
        self.list = arr
        self.min_val = min(arr)
        self.max_val = max(arr)
        self.block_width = round((self.width - self.SIDE_PADDING) / len(arr))
        self.block_height = math.floor((self.height - self.TOP_PADDING) / (self.max_val - self.min_val))
        self.start_x = self.SIDE_PADDING // 2

    def set_order(self, order):
        self.sort_order = order

    def set_algorithm(self, algo_name, algo_fn):
        self.algo_name = algo_name
        self.algorithm = algo_fn