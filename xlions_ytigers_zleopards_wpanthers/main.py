from enum import Enum
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
    def _call_level(self, remove_animal, animals):
        sum = 0
        animal_enum_list = list(Animal)
        if remove_animal is not None:
            animal_enum_list.remove(remove_animal)
        for anim in animal_enum_list:
            animals_cpy = animals.copy()
            animals_cpy[anim.value] -= 1
            sum += self._explore(anim, animals_cpy)
        return sum

    def _explore(self, last_animal, animals):
        zero_found = 0
        for anim_count in animals:
            if anim_count < 0:
                return 0
            elif anim_count == 0:
                zero_found += 1
        if zero_found == len(animals):
            return 1
        return self._call_level(last_animal, animals)

    def solve(self, xlions: int, ytigers: int, zleopards: int, wpanthers: int):
        animals = [xlions, ytigers, zleopards, wpanthers]
        return self._call_level(None, animals)
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
