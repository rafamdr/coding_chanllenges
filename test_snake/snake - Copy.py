from enum import Enum
import random
# ----------------------------------------------------------------------------------------------------------------------


class SnakeDirection(Enum):
    UP = 0,
    RIGHT = 1,
    DOWN = 2,
    LEFT = 3
# ----------------------------------------------------------------------------------------------------------------------


class SnakeBorderException(Exception):
    pass
# ----------------------------------------------------------------------------------------------------------------------


class SnakeSpineException(Exception):
    pass
# ----------------------------------------------------------------------------------------------------------------------

class Snake:

    def __init__(self,
                 screen_width: int,
                 screen_height: int,
                 initial_size: int = 3,
                 initial_direction: SnakeDirection = SnakeDirection.RIGHT):

        self.screen_width = screen_width
        self.screen_height = screen_height
        self._direction = initial_direction
        self._spine = []
        self._internal_map = {}
        self.food_pos = (-1, -1)
        self.food_eaten = initial_size
        self._add_spine(nblocks=initial_size)
        self._add_food()
        self.valid = True

    def get_spine(self):
        return self._spine

    def _eat(self):
        pass

    def update(self):
        self._internal_map = {}
        new_point = self._get_new_point(self._spine[len(self._spine) - 1], self._direction)

        for i in range(0, len(self._spine) - 1):
            self._spine[i] = self._spine[i + 1]
            self._internal_map[self._spine[i]] = 1

        if new_point in self._spine:
            raise SnakeSpineException()

        self._spine[len(self._spine) - 1] = new_point
        self._internal_map[len(self._spine) - 1] = 1

        if new_point == self.food_pos:
            self._add_spine(1)
            self._add_food()

    def _get_new_point(self, last_position, new_direction):
        new_position = last_position

        if new_direction == SnakeDirection.UP:
            new_position = (last_position[0], last_position[1] - 1)
        elif new_direction == SnakeDirection.RIGHT:
            new_position = (last_position[0] + 1, last_position[1])
        elif new_direction == SnakeDirection.DOWN:
            new_position = (last_position[0], last_position[1] + 1)
        elif new_direction == SnakeDirection.LEFT:
            new_position = (last_position[0] - 1, last_position[1])

        if (
                (new_position[0] < 0) or (new_position[0] >= self.screen_width) or
                (new_position[1] < 0) or (new_position[1] >= self.screen_height)
        ):
            raise SnakeBorderException()

        return new_position

    def _add_spine(self, nblocks=1):
        if len(self._spine) == 0:
            last_position = (self.screen_width/2, self.screen_height/2)
        else:
            last_position = self._spine[-1]
        for i in range(0, nblocks):
            new_position = self._get_new_point(last_position, self._direction)
            self._spine.append(new_position)
            self._internal_map[new_position] = 1
            last_position = new_position

    def _add_food(self):
        temp_food_pos = (random.randint(0, self.screen_width - 1), random.randint(0, self.screen_height - 1))

        while temp_food_pos in self._internal_map:
            temp_food_pos = (random.randint(0, self.screen_width - 1), random.randint(0, self.screen_height - 1))

        self._internal_map[temp_food_pos] = 2
        self.food_pos = temp_food_pos
        self.food_eaten = self.food_eaten + 1

    def change_direction(self, new_direction: SnakeDirection):
        if(
                not (
                    (new_direction == SnakeDirection.LEFT and self._direction == SnakeDirection.RIGHT) or
                    (new_direction == SnakeDirection.RIGHT and self._direction == SnakeDirection.LEFT) or
                    (new_direction == SnakeDirection.DOWN and self._direction == SnakeDirection.UP) or
                    (new_direction == SnakeDirection.UP and self._direction == SnakeDirection.DOWN)
                )
        ):
            self._direction = new_direction
# ----------------------------------------------------------------------------------------------------------------------
