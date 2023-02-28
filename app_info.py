import pygame
import math


class AppInfo:
    """
    Configuration of app's information and constants

    Init params:
    :param width: int - width of program's window in pixels
    :param height: int - height of program's window in pixels
    :param arr: list[int] - list of numbers
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


    def __init__(self, width, height, arr):
        self.width = width
        self.height = height
        self.window = pygame.display.set_mode((width, height))
        pygame.display.set_caption('Sorting Algorithms Visualizer')
        self.set_list(arr)

    def set_list(self, arr):
        self.list = arr
        self.min_val = min(arr)
        self.max_val = max(arr)
        self.block_width = round((self.width - self.SIDE_PADDING) / len(arr))
        self.block_height = math.floor((self.height - self.TOP_PADDING) / (self.max_val - self.min_val))
        self.start_x = self.SIDE_PADDING // 2