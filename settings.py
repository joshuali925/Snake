class Settings():
    # all integers
    width = 320
    height = 320
    resolution = width, height
    bg_color = (230, 230, 230)

    snake_size = 20
    snake_color = (60, 60, 60)
    snake_head_color = (0, 0, 255)
    snake_speed = snake_size + 1
    snake_grow_rate = 3
    snake_init_length = 5

    food_size = snake_size
    food_color = (255, 70, 30)
    
    wall_size = 2
    wall_color = (50, 50, 50)

    # dynamic
    all_x = []
    all_y = []
    num_points_reachable = 0
    ai = None
