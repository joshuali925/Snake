import random
import pygame
from settings import Settings


class Food():
    def __init__(self, screen, snake):
        self.screen = screen
        self.snake = snake
        self.x = self.random_x()
        self.y = self.random_y()
        self.rect = pygame.Rect(self.x, self.y,
                                Settings.food_size, Settings.food_size)

    # random returns a point snaps to the grid (reachable for the snake)
    def random_x(self):
        x = random.randint(Settings.food_size,
                           Settings.width - Settings.food_size)
        return (x - self.screen.get_rect().centerx) // Settings.snake_speed * Settings.snake_speed + self.screen.get_rect().centerx

    def random_y(self):
        y = random.randint(Settings.food_size,
                           Settings.height - Settings.food_size)
        return (y - self.screen.get_rect().centery) // Settings.snake_speed * Settings.snake_speed + self.screen.get_rect().centery
        
    def draw(self):
        self.rect.x = self.x
        self.rect.y = self.y
        self.screen.fill(Settings.food_color, self.rect)

    def update(self):
        if self.snake.x[0] == self.x and self.snake.y[0] == self.y:
            self.snake.grow(self.x, self.y)
            self.x = self.random_x()
            self.y = self.random_y()
        self.draw()
