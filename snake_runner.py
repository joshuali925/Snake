import time
import sys
import pygame
from settings import Settings
from snake import Snake
from food import Food
from ai import Ai
from wall import Wall


def generate_all_positions(screen):
    for x in range(Settings.snake_speed, Settings.width - Settings.snake_speed, Settings.snake_speed):
        Settings.all_x.append((x - screen.get_rect().centerx) // Settings.snake_speed *
                              Settings.snake_speed + screen.get_rect().centerx)
    for y in range(Settings.snake_speed, Settings.height - Settings.snake_speed, Settings.snake_speed):
        Settings.all_y.append((y - screen.get_rect().centery) // Settings.snake_speed *
                              Settings.snake_speed + screen.get_rect().centery)
    Settings.num_points_reachable = len(Settings.all_x) * len(Settings.all_y)


def check_events(screen, snake):
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake.direction != 2:
                snake.direction = 1
            elif event.key == pygame.K_DOWN and snake.direction != 1:
                snake.direction = 2
            elif event.key == pygame.K_LEFT and snake.direction != 4:
                snake.direction = 3
            elif event.key == pygame.K_RIGHT and snake.direction != 3:
                snake.direction = 4
            elif event.key == pygame.K_p:
                snake.direction = 0
            elif event.key == pygame.K_q:
                sys.exit()
        elif event.type == pygame.QUIT:
            sys.exit()


def update(screen, snake, food, ai, wall):
    screen.fill(Settings.bg_color)
    wall.update()
    ai.update()
    food.update()
    snake.update()
    pygame.display.flip()


def run():
    pygame.init()
    screen = pygame.display.set_mode(Settings.resolution)
    pygame.display.set_caption('Snake')
    generate_all_positions(screen)

    wall = Wall(screen)
    snake = Snake(screen)
    food = Food(screen, snake)
    ai = Ai(screen, snake, food)
    Settings.ai = ai

    Settings.ai.get_shortest_path(food.rect.x, food.rect.y)
    Settings.ai.set_new_path()
    

    while True:
        check_events(screen, snake)
        update(screen, snake, food, ai, wall)
        time.sleep(0.01)

run()
