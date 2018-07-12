import sys
import pygame
from settings import Settings


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
            elif event.key == pygame.K_q:
                sys.exit()
        elif event.type == pygame.QUIT:
            sys.exit()


def update(screen, snake, food):
    screen.fill(Settings.bg_color)
    food.update()
    snake.update()
    pygame.display.flip()
