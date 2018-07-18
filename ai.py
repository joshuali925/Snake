import pygame
from settings import Settings
import time
import queue as Q


class Ai():
    def __init__(self, screen, snake, food):
        self.screen = screen
        self.snake = snake
        self.food = food
        self.length = self.snake.length

    def set_new_path(self):
        target_x, target_y = self.food.get_position()
        moves = self.get_path(target_x, target_y)
        if len(moves) == 0:
            head_x, head_y = self.snake.get_head_position()
            directions = self.snake.movable_directions(head_x, head_y)
            print("path not found for:", head_x,
                  head_y, "->", target_x, target_y)
            print("possible directions =", directions)
            moves = [directions[0]] if len(directions) > 0 else moves
            if not moves:
                time.sleep(3)
        self.snake.moves = moves

    def update(self):
        pass

    def highlight(self, nodes):
        for n in nodes:
            rect = pygame.Rect(
                n[0], n[1], Settings.food_size, Settings.food_size)
            self.screen.fill((73, 139, 167), rect)
        time.sleep(0.01)

    def get_shortest_path(self, target_x, target_y):  # BFS
        visited = set()
        queue = []
        head_x, head_y = self.snake.get_head_position()
        queue.append((head_x, head_y, []))
        while len(queue) > 0:
            x, y, path = queue.pop(0)
            # self.highlight(visited)
            if x == target_x and y == target_y:
                print("shortest path found with", len(path), "steps")
                return path
            if (x, y) not in visited:
                visited.add((x, y))
                directions = self.snake.movable_directions(x, y)
                for d in directions:
                    next_x, next_y = self.snake.get_move_result(x, y, d)
                    queue.append((next_x, next_y, path + [d]))
        return []

    def get_path(self, target_x, target_y):  # a* algorithm
        visited = set()
        queue = Q.PriorityQueue()
        head_x, head_y = self.snake.get_head_position()
        queue.put((0, head_x, head_y, [], 0))
        while not queue.empty():
            _, x, y, path, g_cost = queue.get()
            if x == target_x and y == target_y:
                print("a* path found with", len(path), "steps")
                return path
            if (x, y) not in visited:
                visited.add((x, y))
                directions = self.snake.movable_directions(x, y)
                for d in directions:
                    next_x, next_y = self.snake.get_move_result(x, y, d)
                    f_cost = self.heuristic(next_x, next_y) + g_cost + 1
                    queue.put((f_cost, next_x, next_y, path + [d], g_cost + 1))
        return []

    def get_path2(self, target_x, target_y):  # a* algorithm
        visited = set()
        queue = Q.PriorityQueue()
        head_x, head_y = self.snake.get_head_position()
        queue.put((0, head_x, head_y, [], 0))
        visited.add((head_x, head_y))
        while not queue.empty():
            _, x, y, path, g_cost = queue.get()
            if x == target_x and y == target_y:
                print("a* path found with", len(path), "steps")
                return path
            directions = self.snake.movable_directions(x, y)
            for d in directions:
                next_x, next_y = self.snake.get_move_result(x, y, d)
                if (next_x, next_y) not in visited:
                    visited.add((next_x, next_y))
                    f_cost = self.heuristic(next_x, next_y) + g_cost + 1
                    queue.put((f_cost, next_x, next_y, path + [d], g_cost + 1))
        return []

    def heuristic(self, x, y):  # manhattan distance
        food_x, food_y = self.food.get_position()
        return abs(x - food_x) + abs(y - food_y)
