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
        target_x, target_y = self.food.get_position()
        moves = self.get_path(target_x, target_y)
        if len(moves) == 0:
            print("path not found")
            head_x, head_y = self.snake.get_head_position()
            directions = self.snake.movable_directions(head_x, head_y)
            print("possible directions =", directions)
            moves = [directions[0]] if len(directions) > 0 else moves
        self.snake.moves = moves

    def update(self):
        pass

    def get_path(self, target_x, target_y):
        visited = set()
        queue = Q.PriorityQueue()
        head_x, head_y = self.snake.get_head_position()
        queue.put((0, head_x, head_y, []))
        while not queue.empty():
            _, x, y, path = queue.get()
            if x == target_x and y == target_y:
                return path
            if (x, y) not in visited:
                visited.add((x, y))
                directions = self.snake.movable_directions(x, y)
                for d in directions:
                    next_x, next_y = self.snake.get_move_result(x, y, d)
                    p = self.get_priority(next_x, next_y)
                    queue.put((p, next_x, next_y, path + [d]))
        return []

    def get_priority(self, x, y):  # manhattan distance
        food_x, food_y = self.food.get_position()
        return abs(x - food_x) + abs(y - food_y)
