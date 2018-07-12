import sys
import pygame
from settings import Settings


def check_events(screen, snake):
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                snake.direction = 1
            elif event.key == pygame.K_DOWN:
                snake.direction = 2
            elif event.key == pygame.K_LEFT:
                snake.direction = 3
            elif event.key == pygame.K_RIGHT:
                snake.direction = 4
            elif event.key == pygame.K_q:
                sys.exit()
        elif event.type == pygame.QUIT:
            sys.exit()


def update(screen, snake, food):
    screen.fill(Settings.bg_color)
    snake.update()
    food.update()
    pygame.display.flip()
