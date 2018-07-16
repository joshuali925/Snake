import pygame
from settings import Settings
import time
import queue as Q


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
        queue = Q.PriorityQueue()
        head_x, head_y = self.snake.get_head_position()
        queue.put((0, head_x, head_y, []))
        # queue.append((head_x, head_y, []))
        while not queue.empty():
            _, x, y, path = queue.get()
            food_x, food_y = self.food.get_position()
            print(x, y, head_x, head_y, food_x, food_y,  path)
            if x == food_x and y == food_y:
                return path
            if (x, y) not in visited:
                visited.add((x, y))
                directions = self.snake.movable_directions(x, y)
                for d in directions:
                    next_x, next_y = self.snake.move(x, y, d)
                    priority = self.get_priority(next_x, next_y)
                    queue.put((priority, next_x, next_y, path + [d]))
        print("path not found")
        print(x, y, head_x, head_y, food_x, food_y, path)
        directions = self.snake.movable_directions(head_x, head_y)
        print("possible directions =", directions)
        return directions[:1] + [0] if len(directions) > 0 else [0]

    def get_priority(self, x, y):
        food_x, food_y = self.food.get_position()
        return abs(x - food_x) + abs(y - food_y)
