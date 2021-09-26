from enum import Enum
import numpy as np
# ----------------------------------------------------------------------------------------------------------------------


"""There are x lions, y tigers, z leopards, and w panthers. Find the number of ways to place them on a line such that
no two same animals are adjacent to each other (assume w, x, y, and z are <= 50). """
# ----------------------------------------------------------------------------------------------------------------------


class Animal(Enum):
    LION = 0
    TIGER = 1
    LEOPARD = 2
    PANTHER = 3
# ----------------------------------------------------------------------------------------------------------------------


class Solution:
    MAX = 50

    def __init__(self):
        self.dp = None

    def _call_levels(self, remove_animal, animals):
        sum_ways = 0
        animal_enum_list = list(Animal)
        animals_cpy = animals.copy()
        if remove_animal is not None:
            animal_enum_list.remove(remove_animal)
            animals_cpy[remove_animal.value] -= 1
        for anim in animal_enum_list:
            sum_ways += self._getNumberAnimalsLineWays(anim, animals_cpy)
        return sum_ways

    def _getNumberAnimalsLineWays(self, last_animal, animals):
        zero_found = 0
        for anim in Animal:
            if animals[anim.value] < 0:
                return 0
            elif animals[anim.value] == 0:
                zero_found += 1
        if animals[last_animal.value] == 1 and zero_found == len(animals) - 1:
            return 1
        li_idx = animals[Animal.LION.value]
        ti_idx = animals[Animal.TIGER.value]
        le_idx = animals[Animal.LEOPARD.value]
        pa_idx = animals[Animal.PANTHER.value]
        if self.dp[li_idx][ti_idx][le_idx][pa_idx][last_animal.value] != -1:
            return self.dp[li_idx][ti_idx][le_idx][pa_idx][last_animal.value]
        self.dp[li_idx][ti_idx][le_idx][pa_idx][last_animal.value] = self._call_levels(last_animal, animals)
        return self.dp[li_idx][ti_idx][le_idx][pa_idx][last_animal.value]

    def solve(self, xlions: int, ytigers: int, zleopards: int, wpanthers: int):
        self.dp = np.full((50, 50, 50, 50, 50), -1, dtype='int64')
        animals = [xlions, ytigers, zleopards, wpanthers]
        return self._call_levels(None, animals)
# ----------------------------------------------------------------------------------------------------------------------


sol = Solution()
print(sol.solve(0, 0, 0, 0))
print(sol.solve(1, 0, 0, 0))
print(sol.solve(1, 1, 0, 0))
print(sol.solve(1, 1, 1, 0))
print(sol.solve(1, 1, 1, 1))
print(sol.solve(2, 2, 2, 2))
print(sol.solve(20, 10, 8, 12))
# ----------------------------------------------------------------------------------------------------------------------
