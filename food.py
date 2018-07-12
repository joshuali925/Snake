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

    def random_x(self):
        return random.randint(Settings.food_size, Settings.width - Settings.food_size)

    def random_y(self):
        return random.randint(Settings.food_size, Settings.height - Settings.food_size)

    def draw(self):
        self.rect = pygame.Rect(self.x, self.y,
                           Settings.food_size, Settings.food_size)
        self.screen.fill(Settings.food_color, self.rect)
        
        
    def update(self):
        snake_rect = pygame.Rect(self.snake.x[0], self.snake.y[0], Settings.snake_length, Settings.snake_length)
        if snake_rect.colliderect(self.rect):
            self.snake.grow(self.x, self.y)
            self.x = self.random_x()
            self.y = self.random_y()
        self.draw()