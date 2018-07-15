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
        self.direction = 0  # 1 = up, 2 = down, 3 = left, 4 = right, 0 = stop

    def draw(self):
        for i in range(1, self.length):
            self.screen.fill(Settings.snake_color, self.body[i])
        self.screen.fill(Settings.snake_head_color, self.body[0])

    def update(self):
        self.draw()
        if self.direction == 0:
            return
        self.check_bounds()
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

    def check_bounds(self):
        if self.body[0].y <= Settings.all_y[0] and self.direction == 1:
            self.direction = 3
        if self.body[0].y >= Settings.all_y[-1] and self.direction == 2:
            self.direction = 4
        if self.body[0].x <= Settings.all_x[0] and self.direction == 3:
            self.direction = 2
        if self.body[0].x >= Settings.all_x[-1] and self.direction == 4:
            self.direction = 1

    def grow(self):
        for _ in range(Settings.snake_grow_rate):
            self.body.append(pygame.Rect(
                self.body[-1].x, self.body[-1].y, Settings.snake_size, Settings.snake_size))
        self.length += Settings.snake_grow_rate

    def at_point(self, x, y):
        for rect in self.body:
            if rect.x == x and rect.y == y:
                return True
        return False
    
    def head_at_point(self, x, y):
        return self.body[0].x == x and self.body[0].y == y