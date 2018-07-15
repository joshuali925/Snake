import random
import pygame
from settings import Settings


class Food():
    def __init__(self, screen, snake):
        self.screen = screen
        self.snake = snake
        self.rect = pygame.Rect(0, 0, Settings.food_size, Settings.food_size)
        self.set_random_point()
        self.ai = None
        self.new_food = False

    # random returns a point snaps to the grid (reachable for the snake)
    def set_random_point(self):
        if Settings.num_points_reachable == self.snake.length:
            return
        n = random.randint(0, Settings.num_points_reachable - 1)
        x_i = n // len(Settings.all_x)
        y_i = n % len(Settings.all_y)
        x, y = Settings.all_x[x_i], Settings.all_y[y_i]
        if self.snake.at_point(x, y):
            self.set_random_point()
        else:
            self.rect.x, self.rect.y = x, y

    def update(self):
        if self.new_food is True:
            self.ai.set_new_path()
            self.new_food = False
        if self.snake.head_at_point(self.rect.x, self.rect.y):
            self.set_random_point()
            self.snake.grow()
            self.new_food = True
        self.screen.fill(Settings.food_color, self.rect)

    def get_position(self):
        return self.rect.x, self.rect.y