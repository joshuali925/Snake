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
        self.moves = []

    def draw(self):
        for i in range(1, self.length):
            self.screen.fill(Settings.snake_color, self.body[i])
        self.screen.fill(Settings.snake_head_color, self.body[0])

    def update(self):
        # Settings.ai.set_new_path()
        self.direction = self.moves.pop(0) if len(self.moves) > 0 else 0
        if self.direction != 0:
            self.check_bounds()
            self.move(self.direction)
        self.draw()
    
    def move(self, direction):
        for i in range(self.length - 1, 0, -1):
            self.body[i].x = self.body[i - 1].x
            self.body[i].y = self.body[i - 1].y
        x, y = self.get_move_result(
            self.body[0].x, self.body[0].y, direction)
        self.body[0].x, self.body[0].y = x, y

    def check_bounds(self):
        if self.body[0].y <= Settings.all_y[0] and self.direction == 1:
            self.direction = 3
        elif self.body[0].y >= Settings.all_y[-1] and self.direction == 2:
            self.direction = 4
        elif self.body[0].x <= Settings.all_x[0] and self.direction == 3:
            self.direction = 2
        elif self.body[0].x >= Settings.all_x[-1] and self.direction == 4:
            self.direction = 1
        else:
            return False
        return True

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

    def get_move_result(self, x, y, direction):
        if direction == 1:
            y -= Settings.snake_speed
        elif direction == 2:
            y += Settings.snake_speed
        elif direction == 3:
            x -= Settings.snake_speed
        elif direction == 4:
            x += Settings.snake_speed
        return (x, y)

    def can_move(self, x, y, direction):
        next_x, next_y = self.get_move_result(x, y, direction)
        return next_x >= Settings.all_x[0] and next_x <= Settings.all_x[-1] and next_y >= Settings.all_y[0] and next_y <= Settings.all_y[-1] and not self.at_point(next_x, next_y)

    def movable_directions(self, x, y):
        directions = []
        for d in range(1, 5):
            if self.can_move(x, y, d):
                directions.append(d)
        return directions

    def get_head_position(self):
        return self.body[0].x, self.body[0].y

    def get_tail_position(self):
        return self.body[-1].x, self.body[-1].y
