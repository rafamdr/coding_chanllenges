# Given a list of folders in a filesystem and the name of a folder to remove, return the new list of folders after
# removal.
#
# Examples:
# $ removeFolder(['/a', '/a/b', '/c/d', '/c/d/e', '/c/f', '/c/f/g'], 'c')
# $ ['/a','/a/b']
# $ removeFolder(['/a', '/a/b', '/c/d', '/c/d/e', '/c/f', '/c/f/g'], 'd')
# $ ['/a', '/a/b', '/c', '/c/f', '/c/f/g']
# ----------------------------------------------------------------------------------------------------------------------


from functools import reduce
from typing import List
# ----------------------------------------------------------------------------------------------------------------------


class DirNode:
    def __init__(self):
        self.children = set()
        self.is_final = False
# ----------------------------------------------------------------------------------------------------------------------


class Solution:
    def remove_folder_ref(self, paths: List[str], dir_to_remove: str) -> List[str]:
        result = set()
        for path in paths:
            result_path = ''
            splited_path = path.split('/')
            for dir in splited_path[1:]:
                if dir == dir_to_remove:
                    break
                result_path += '/' + dir
            if result_path != '':
                result.add(result_path)
        return sorted(list(result))

    def remove_folder_small(self, paths: List[str], dir_to_remove: str) -> List[str]:
        result = set()
        temp_set = set(arr)
        return reduce(lambda count, number: count + int(number + diff in temp_set), arr, 0)
        # return sorted(list(result))
        return []

    def remove_folder_fancy(self, paths: List[str], dir_to_remove: str) -> List[str]:
        graph = {'/': DirNode()}
        for path in paths:
            splited_path = path.split('/')
            above_level = '/'
            for dir in splited_path[1:]:
                if dir == dir_to_remove:
                    break
                if dir not in graph:
                    graph[dir] = DirNode()
                graph[above_level].children.add(dir)
                above_level = dir
            if above_level != '/':
                graph[above_level].is_final = True
        result = []
        stack = [['', '/']]
        while len(stack) > 0:
            prt, dir = stack.pop()
            for child in graph[dir].children:
                concat = prt + '/' + child
                if len(graph[child].children) == 0 or graph[child].is_final:
                    result.append(concat)
                stack.append([concat, child])
        return sorted(result)
# ----------------------------------------------------------------------------------------------------------------------


examples = {
    (('/a', '/a/b', '/c/d', '/c/d/e', '/c/f', '/c/f/g'), 'c'): ['/a', '/a/b'],
    (('/a', '/a/b', '/c/d', '/c/d/e', '/c/f', '/c/f/g'), 'd'): ['/a', '/a/b', '/c', '/c/f', '/c/f/g'],
}


sol = Solution()

for ex in examples:
    print('Ref...: %s -> %s ' % (str(ex), sol.remove_folder_ref(list(ex[0]), ex[1])))
    print('Small.: %s -> %s ' % (str(ex), sol.remove_folder_ref(list(ex[0]), ex[1])))
    print('Fancy.: %s -> %s ' % (str(ex), sol.remove_folder_fancy(list(ex[0]), ex[1])))
    print()
# ----------------------------------------------------------------------------------------------------------------------
