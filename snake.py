import pygame
from settings import Settings


class Snake():
    def __init__(self, screen):
        self.screen = screen
        self.x = [screen.get_rect().centerx] * Settings.snake_init_length
        self.y = [screen.get_rect().centery] * Settings.snake_init_length
        self.length = Settings.snake_init_length
        self.direction = 0  # 1 = up, 2 = down, 3 = left, 4 = right

    def draw_at(self, x, y):
        rect = pygame.Rect(x, y, Settings.snake_size, Settings.snake_size)
        self.screen.fill(Settings.snake_color, rect)

    def update(self):
        for i in range(self.length):
            self.draw_at(self.x[i], self.y[i])
        if self.direction == 0:
            return
        for i in range(self.length - 1, 0, -1):
            self.x[i] = self.x[i - 1]
            self.y[i] = self.y[i - 1]
        # 4=3, 3=2, 2=1, 1=0, modify 0
        if self.direction == 1:
            self.y[0] -= Settings.snake_speed
        elif self.direction == 2:
            self.y[0] += Settings.snake_speed
        elif self.direction == 3:
            self.x[0] -= Settings.snake_speed
        elif self.direction == 4:
            self.x[0] += Settings.snake_speed

    def grow(self):
        for _ in range(Settings.snake_grow_rate):
            self.x.append(self.x[-1])
            self.y.append(self.y[-1])
        self.length += Settings.snake_grow_rate