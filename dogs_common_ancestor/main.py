from typing import Dict
# ----------------------------------------------------------------------------------------------------------------------


class Dog:
    def __init__(self, name: str, age: int, data: Dict = None):
        if data is None:
            self.name = name
            self.age = age
        else:
            self.name = data['name']
            self.age = data['age']
# ----------------------------------------------------------------------------------------------------------------------


class Relation:
    def __init__(self, dog: Dog):
        self.dog = dog
        self.children = set()
# ----------------------------------------------------------------------------------------------------------------------


class Relationship:
    def __init__(self):
        self.graph = {}

    def _check_parent(self, parent_name: str, child):
        if parent_name:
            if parent_name not in self.graph:
                self.add_dog(Dog(parent_name, 0), None, None)
            self.graph[parent_name].children.add(child.name)

    def add_dog(self, dog: Dog, mother_name: str, father_name: str):
        self.graph[dog.name] = Relation(dog)
        self._check_parent(mother_name, dog)
        self._check_parent(father_name, dog)

    def _dfs(self, expected_name: str):
        visited = set()
        main_seq = set()
        seq = []
        stack = []
        for item in self.graph.keys():
            stack.append([item, 0])
            visited = set()
            seq = []
            while len(stack) > 0:
                curr = stack.pop()
                while len(seq) > 0:
                    if seq[-1][1] >= curr[1]:
                        seq.pop()
                    else:
                        break
                if curr[0] == expected_name:
                    for nn in seq:
                        main_seq.add(nn[0])
                else:
                    visited.add(tuple(curr))
                    seq.append(tuple(curr))
                    for item in self.graph[curr[0]].children:
                        if item not in visited:
                            stack.append([item, curr[1] + 1])
        return main_seq

    def check_common_ancestors(self, a: str, b: str):
        if a not in self.graph or b not in self.graph:
            return None
        ancs_a = self._dfs(a)
        ancs_b = self._dfs(b)
        return list(ancs_a.intersection(ancs_b))
# ----------------------------------------------------------------------------------------------------------------------


relship = Relationship()
relship.add_dog(
    Dog('Bruce Wayne', 1),
    'Martha Kane',
    'Thomas Wayne',
)
relship.add_dog(
    Dog('Philip Wayne', 3),
    'Martha Kane',
    'Thomas Wayne',
)
relship.add_dog(
    Dog('Helena Wayne', 1),
    'Selina Kyle',
    'Bruce Wayne',
)
relship.add_dog(
    Dog('Jonathan Kent', 9),
    'Jessica Kent',
    'Hiram Kent',
)
relship.add_dog(
    Dog('Clark Kent', 2),
    'Martha Kane',
    'Jonathan Kent',
)
relship.add_dog(
    Dog('Jonathan Samuel Kent', 1),
    'Louis Lane',
    'Clark Kent',
)

print(relship.check_common_ancestors('asdasd', 'Helena Wayne'))
print(relship.check_common_ancestors('Jonathan Samuel Kent', 'Helena Wayne'))
print(relship.check_common_ancestors('Louis Lane', 'Helena Wayne'))
print(relship.check_common_ancestors('Philip Wayne', 'Bruce Wayne'))
# ----------------------------------------------------------------------------------------------------------------------
