# Implement a hashmap from scratch without any existing libraries in your preferred language.
#
# A hashmap should:
#
# - Be empty when initialized
# - Have the function put(int key, int value) which inserts a (key, value) pair into the
# hashmap. If the key already exists, update the corresponding value.
# - Have the function get(int key) which returns
# the value to which the specified key is mapped, or -1 if there’s no mapping for the key.
# - Have the function remove(key) which removes the key and its value if it exists in the map.
# ----------------------------------------------------------------------------------------------------------------------


from collections import deque
# ----------------------------------------------------------------------------------------------------------------------


class HashMap:
    MAX_ARRAY_SIZE = 64
    ELEM_NOT_FOUND = -1

    def __init__(self):
        self.array = []

    def _get_pos(self, key: int) -> int:
        return key % HashMap.MAX_ARRAY_SIZE

    def put(self, key: int, value: int):
        idx = self._get_pos(key)
        if idx >= len(self.array):
            for _ in range(0, idx - len(self.array) + 1):
                self.array.append(deque([]))
        cell = self.array[idx]
        for _ in range(0, len(cell)):
            item = cell.popleft()
            if item[0] == key:
                break
            cell.append(item)
        cell.append((key, value))

    def get(self, key: int) -> int:
        if (idx := self._get_pos(key)) < len(self.array):
            cell = self.array[idx]
            for _ in range(0, len(cell)):
                cell.append(item := cell.popleft())
                if item[0] == key:
                    return item[-1]
        return HashMap.ELEM_NOT_FOUND

    def remove(self, key: int):
        if (idx := self._get_pos(key)) < len(self.array):
            cell = self.array[idx]
            for _ in range(0, len(cell)):
                item = cell.popleft()
                if item[0] == key:
                    break
                cell.append(item)

    def __str__(self):
        return '{%s}' % ', '.join([f'{k}: {v}' for l in self.array for k, v in l])
# ----------------------------------------------------------------------------------------------------------------------


examples = {
    1: [
        ('put', {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}),
        ('get', [1, 2, 3, 4, 5, 6]),
        ('remove', [2, 3]),
        ('__str__', '{1: 10, 4: 40, 5: 50, 6: 60}')
    ],

    2: [
        ('put', {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}),
        ('put', {1: 100, 2: 200}),
        ('get', [1, 2, 3, 4, 5, 6]),
        ('remove', [5, 4]),
        ('__str__', '{1: 100, 2: 200, 3: 30, 6: 60}')
    ],

    21: [
        ('put', {6: 60, 1: 10, 2: 20, 3: 30, 4: 40, 5: 50}),
        ('put', {1: 100, 2: 200}),
        ('get', [1, 2, 3, 4, 5, 6]),
        ('remove', [5, 4, 40]),
        ('__str__', '{1: 100, 2: 200, 3: 30, 6: 60}')
    ],

    3: [
        ('put', {0: 10, 64: 20}),
        ('remove', [64]),
        ('__str__', '{0: 10}')
    ],
}


for ex in examples:
    sol = globals()['HashMap']()
    methods = examples[ex]
    str_result = ''
    for method, values in methods:
        if type(values) == dict:
            for key, elem in values.items():
                getattr(sol, method)(key, elem)
        elif type(values) == list:
            for value in values:
                getattr(sol, method)(value)
        else:
            str_result = values
    print('Ref..: %s -> %s ' % (str_result, str(sol)))
    print()
# ----------------------------------------------------------------------------------------------------------------------
