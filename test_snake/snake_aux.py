import pygame
from snake import Snake, SnakeDirection
# ----------------------------------------------------------------------------------------------------------------------


def key_ev_to_snake_dir(key_event):
    if key_event == pygame.K_UP:
        return SnakeDirection.UP
    elif key_event == pygame.K_RIGHT:
        return SnakeDirection.RIGHT
    elif key_event == pygame.K_DOWN:
        return SnakeDirection.DOWN
    elif key_event == pygame.K_LEFT:
        return SnakeDirection.LEFT
    else:
        return None
# ----------------------------------------------------------------------------------------------------------------------
