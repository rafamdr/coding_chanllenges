# importing libraries
import pygame
from pygame.locals import *
import random
from snake import Snake, SnakeDirection
from snake_aux import key_ev_to_snake_dir
# ----------------------------------------------------------------------------------------------------------------------

pygame.init()

window_size = [900, 600]
pixels_per_block = 10
screen = pygame.display.set_mode(window_size)

title = "Snake"

pygame.display.set_caption(title)

clock = pygame.time.Clock()

white = (255, 255, 255)
red = (255, 0, 0)

snake_width = int(window_size[0] / pixels_per_block)
snake_height = int(window_size[1] / pixels_per_block)
max_blocks = snake_width * snake_height

snake1 = Snake(snake_width, snake_height, 4, SnakeDirection.RIGHT)

TICK_INITIAL_INTERVAL = 200


def get_tick_interval(food_eaten):
    result = int(TICK_INITIAL_INTERVAL * ((max_blocks - food_eaten * 64) / max_blocks))
    if result <= 0:
        return 1
    return result


while snake1.valid:
    tick_interval = get_tick_interval(snake1.food_eaten)

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            dir = key_ev_to_snake_dir(event.key)
            if dir is not None:
                snake1.change_direction(dir)
                break
        if event.type == pygame.QUIT:
            exit(0)

    screen.fill((0, 0, 0))
    for point in snake1.get_spine():
        temp_rect = pygame.Rect(
            (point[0] * pixels_per_block, point[1] * pixels_per_block),
            (pixels_per_block, pixels_per_block)
        )
        pygame.draw.rect(screen, white, temp_rect)

    temp_rect = pygame.Rect(
        (snake1.food_pos[0] * pixels_per_block, snake1.food_pos[1] * pixels_per_block),
        (pixels_per_block, pixels_per_block)
    )
    pygame.draw.rect(screen, red, temp_rect)

    snake1.update()
    pygame.display.update()
    pygame.time.wait(tick_interval)
# ----------------------------------------------------------------------------------------------------------------------
