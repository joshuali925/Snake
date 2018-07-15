import pygame
from settings import Settings


class Ai():
    def __init__(self, screen, snake, food):
        self.screen = screen
        self.snake = snake
        self.food = food
        self.set_new_path()
        self.length = self.snake.length

    def set_new_path(self):
        self.snake.moves = self.get_path()
    
    def update(self):
        pass
        
    def get_path(self):
        visited = set()
        queue = []
        x, y = self.snake.get_head_position()
        queue.append((x, y, []))
        while len(queue) > 0:
            x, y, path = queue.pop(0)
            food_x, food_y = self.food.get_position()
            print(x, y, food_x, food_y, path)
            if x == food_x and y == food_y:
                return path
            if (x, y) not in visited:
                visited.add((x, y))
                directions = self.snake.movable_directions()
                for d in directions:
                    next_x, next_y = self.snake.move(x, y, d)
                    queue.append((next_x, next_y, path + [d]))
        return [0]
