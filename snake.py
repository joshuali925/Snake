import pygame
from settings import Settings


class Snake():
    def __init__(self, screen):
        self.screen = screen
        self.body = []  # head is body[0], tail is body[-1]
        for _ in range(Settings.snake_init_length):
            self.body.append(pygame.Rect(screen.get_rect().centerx, screen.get_rect().centery,
                                         Settings.snake_size, Settings.snake_size))
        self.length = Settings.snake_init_length
        self.direction = 0  # 1 = up, 2 = down, 3 = left, 4 = right

    def draw(self):
        for i in range(self.length):
            self.screen.fill(Settings.snake_color, self.body[i])

    def update(self):
        self.draw()
        if self.direction == 0:
            return
        # 4=3, 3=2, 2=1, 1=0, modify 0
        for i in range(self.length - 1, 0, -1):
            self.body[i].x = self.body[i - 1].x
            self.body[i].y = self.body[i - 1].y
        if self.direction == 1:
            self.body[0].y -= Settings.snake_speed
        elif self.direction == 2:
            self.body[0].y += Settings.snake_speed
        elif self.direction == 3:
            self.body[0].x -= Settings.snake_speed
        elif self.direction == 4:
            self.body[0].x += Settings.snake_speed
        self.check_bounds()

    def check_bounds(self):
        if self.body[0].x < -Settings.snake_size or self.body[0].x > Settings.width or self.body[0].y < -Settings.snake_size or self.body[0].y > Settings.height:
            self.direction = 0

    def grow(self):
        for _ in range(Settings.snake_grow_rate):
            self.body.append(pygame.Rect(
                self.body[-1].x, self.body[-1].y, Settings.snake_size, Settings.snake_size))
        self.length += Settings.snake_grow_rate
