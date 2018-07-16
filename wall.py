import pygame
from settings import Settings


class Wall():
    def __init__(self, screen):
        self.screen = screen
        min_x, min_y = Settings.all_x[0], Settings.all_y[0]
        max_x, max_y = Settings.all_x[-1], Settings.all_y[-1]
        self.walls = []
        self.walls.append(pygame.Rect(
            min_x - Settings.wall_size - 1, min_y - Settings.wall_size - 1, max_x - min_x + Settings.snake_speed + Settings.wall_size * 2 + 1, Settings.wall_size))
        self.walls.append(pygame.Rect(
            min_x - Settings.wall_size - 1, min_y - Settings.wall_size - 1, Settings.wall_size, max_y - min_y + Settings.snake_speed + Settings.wall_size * 2 + 1))
        self.walls.append(pygame.Rect(
            max_x + Settings.snake_speed, min_y - Settings.wall_size, Settings.wall_size, max_y - min_y + Settings.snake_speed + Settings.wall_size * 2))
        self.walls.append(pygame.Rect(
            min_x - Settings.wall_size, max_y + Settings.snake_speed, max_x - min_x + Settings.snake_speed + Settings.wall_size * 2, Settings.wall_size))

    def update(self):
        for wall in self.walls:
            self.screen.fill(Settings.wall_color, wall)
