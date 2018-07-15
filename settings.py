class Settings():
    # all integers
    width = 600
    height = 400
    resolution = width, height
    bg_color = (230, 230, 230)

    snake_size = 10
    snake_color = (60, 60, 60)
    snake_head_color = (0, 0, 255)
    snake_speed = 11
    snake_grow_rate = 3
    snake_init_length = 5

    food_size = snake_size
    food_color = (255, 70, 30)
    
    # dynamic
    all_x = []
    all_y = []
    num_points_reachable = 0
