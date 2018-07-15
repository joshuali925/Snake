import pygame
from settings import Settings


class Ai():
    def __init__(self, screen, snake, food):
        self.screen = screen
        self.snake = snake
        self.food = food

    def update(self):
        pass
        # for x in Settings.all_x:
        #     for y in Settings.all_y:
        #         self.screen.fill(Settings.food_color, pygame.Rect(x, y, 1, 1))
