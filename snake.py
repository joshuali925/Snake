import pygame
from settings import Settings


class Snake():
    def __init__(self, screen):
        self.screen = screen
        self.x = [screen.get_rect().centerx] * 5
        self.y = [screen.get_rect().centery] * 5

        self.direction = 0  # 1 = up, 2 = down, 3 = left, 4 = right
        self.length = len(self.x)

    def draw_at(self, x, y):
        rect = pygame.Rect(x, y, Settings.snake_length, Settings.snake_length)
        self.screen.fill(Settings.snake_color, rect)

    def update(self):
        for i in range(self.length):
            self.draw_at(self.x[i], self.y[i])
        if self.direction == 0:
            return
        for i in range(self.length - 1, 0, -1):
            self.x[i] = self.x[i - 1]
            self.y[i] = self.y[i - 1]
        if self.direction == 1:
            self.y[0] -= Settings.snake_speed
        elif self.direction == 2:
            self.y[0] += Settings.snake_speed
        elif self.direction == 3:
            self.x[0] -= Settings.snake_speed
        elif self.direction == 4:
            self.x[0] += Settings.snake_speed

    def grow(self, x, y):
        self.x.insert(0, x)
        self.y.insert(0, y)
        self.length += 1