# Given an array of integers representing asteroids in a row, for each asteroid, the absolute value represents its
# size, and the sign represents its direction (positive = right, negative = left). Return the state of the asteroids
# after all collisions (assuming they are moving at the same speed). If two asteroids meet, the smaller one will
# explode. When they are the same size, they both explode. Asteroids moving in the same direction will never meet.
#
# Example:
#
# $ asteroids([5, 8, -5])
# $ [5, 8] // The 8 and -5 collide, 8 wins. The 5 and 8 never collide.
#
# $ asteroids([10, -10]) $ [] // The 10 and -10 collide and they both explode.
# ----------------------------------------------------------------------------------------------------------------------


from typing import List
# ----------------------------------------------------------------------------------------------------------------------


class Solution:
    BAD_AST = 0xFFFFFFFF
    def asteroid_collision_ref(self, asteroids: List[int]) -> List[int]:
        # O(n^2) with O(n) extra space
        output = []
        i = 0
        last_pos = 0
        while i < len(asteroids):
            while last_pos < len(asteroids) and (asteroids[last_pos] == Solution.BAD_AST or asteroids[last_pos] < 0):
                last_pos += 1
                i = last_pos if i < last_pos else i
            if i < len(asteroids) and asteroids[i] < 0 < asteroids[last_pos]:
                j = i - 1
                while j >= last_pos:
                    if asteroids[j] != Solution.BAD_AST:
                        if abs(asteroids[j]) > abs(asteroids[i]):
                            asteroids[i] = Solution.BAD_AST
                            break
                        elif abs(asteroids[i]) > abs(asteroids[j]):
                            asteroids[j] = Solution.BAD_AST
                        else:
                            asteroids[i] = Solution.BAD_AST
                            asteroids[j] = Solution.BAD_AST
                            break
                    j -= 1
            i += 1

        for ast in asteroids:
            if ast != Solution.BAD_AST:
                output.append(ast)

        return output

    def asteroid_collision_fast1(self, asteroids: List[int]) -> List[int]:
        # O(n)
        i = 0
        last_pos = 0
        while i < len(asteroids):
            while asteroids[last_pos] < 0:
                last_pos += 1
                if last_pos >= len(asteroids):
                    return asteroids
                elif i < last_pos:
                    i = last_pos
            if asteroids[i] < 0 < asteroids[last_pos]:
                j = i - 1
                while j >= last_pos:
                    if abs(asteroids[j]) > abs(asteroids[i]):
                        del asteroids[i]
                        i -= 1
                        break
                    elif abs(asteroids[i]) > abs(asteroids[j]):
                        del asteroids[j]
                        i -= 1
                        j = i - 1
                    else:
                        del asteroids[i]
                        del asteroids[j]
                        i -= 1
                        break
            else:
                i += 1
        return asteroids

    def asteroid_collision_fast2(self, asteroids: List[int]) -> List[int]:
        # O(n) with O(n) extra space (STACK)
        stack = []
        for ast in asteroids:
            while stack and ast < 0 < stack[-1]:
                if stack[-1] < -ast:
                    stack.pop()
                    continue
                elif stack[-1] == -ast:
                    stack.pop()
                break
            else:
                stack.append(ast)
        return stack
# ----------------------------------------------------------------------------------------------------------------------


examples = [
    [1, 1, -1, -2],
    [-2, -2, 1, -2],
    [7, -1, 2, -3, -6, -6, -6, 4, 10, 2],
    [5, 10, -5],
    [8, -8],
    [-8, 8],
    [10, 2, -5],
    [-2, -1, 1, 2],
    [1, 2, 3, -7],
    [1, 7, 2, 3, -7],
    [7, -1, -2, -3],
    [],
    [4],
    [-6],
    [1, 2, 3, 4],
    [4, 3, 2, 1],
    [1, 1, 1]
]

sol = Solution()

for ex in examples:
    print('Ref..: %s -> %s ' % (str(ex), str(sol.asteroid_collision_ref(ex.copy()))))
    print('Fast1: %s -> %s ' % (str(ex), str(sol.asteroid_collision_fast1(ex.copy()))))
    print('Fast2: %s -> %s ' % (str(ex), str(sol.asteroid_collision_fast2(ex))))
    print()
# ----------------------------------------------------------------------------------------------------------------------
