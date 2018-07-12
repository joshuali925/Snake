import pygame
from settings import Settings
import game_functions as gf
from snake import Snake
from food import Food
import time

def run():
    pygame.init()
    screen = pygame.display.set_mode(Settings.resolution)
    pygame.display.set_caption('Snake')
    
    snake = Snake(screen)
    
    food = Food(screen, snake)
    
    while True:
        time.sleep(0.1)
        gf.check_events(screen, snake)
        gf.update(screen, snake, food)
        
run()