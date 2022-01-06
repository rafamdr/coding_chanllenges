# Given a list of Point objects (where a Point object has a name, and a list of names it is connected to),
# a starting Point object, and an ending Point object, return a possible path between the two Points. If there are
# multiple paths, return the shortest one. If there is no path, return “no path”.
#
# Example:
#
# listOfPoints = [
#   { name: "A", connections: ["B", "C"] },
#   { name: "B", connections: ["A", "E"] },
#   { name: "C", connections: ["A", "D"] },
#   { name: "D", connections: ["C"] },
#   { name: "E", connections: ["B", "F"] },
#   { name: "F", connections: ["E"] },
# ]
#
# $ pathBetweenPoints(listOfPoints, "A", "F")
# $ A -> B -> E -> F
#
# $ pathBetweenPoints(listOfPoints, "D", "B")
# $ D -> C -> A -> B
# ----------------------------------------------------------------------------------------------------------------------


# ----------------------------------------------------------------------------------------------------------------------
from typing import List


class Solution:
    def path_between_points_dfs(self, points: List[dict], src: str, dst: str) -> str:
        graph = {point['name']: point['connections'] for point in points}
        visited = set()
        stack = [[src, [src]]]
        result_path = None
        while len(stack) > 0:
            current_point, path = stack.pop()
            if current_point == dst and (result_path is None or len(path) < len(result_path)):
                result_path = path.copy()
            else:
                visited.add(current_point)
                if current_point in graph:
                    for next_point in graph[current_point]:
                        if next_point not in visited:
                            stack.append([next_point, path + [next_point]])
        return 'no path' if result_path is None else ' -> '.join(result_path)

    def path_between_points_bfs(self, points: List[dict], src: str, dst: str) -> str:
        graph = {point['name']: point['connections'] for point in points}
        queue = [[src, [src]]]
        visited = set()
        while len(queue) > 0:
            current_point, path = queue.pop(0)
            if current_point == dst:
                return ' -> '.join(path)
            visited.add(current_point)
            if current_point in graph:
                for next_point in graph[current_point]:
                    if next_point not in visited:
                        queue.append([next_point, path + [next_point]])
        return 'no path'

    def path_between_points_bfs_v2(self, points: List[dict], src: str, dst: str) -> str:
        graph = {point['name']: point['connections'] for point in points}
        if {src, dst}.issubset(graph):
            queue = [[src, [src]]]
            visited = set()
            while len(queue) > 0:
                current_point, path = queue.pop(0)
                if current_point == dst:
                    return ' -> '.join(path)
                visited.add(current_point)
                for next_point in graph[current_point]:
                    if next_point not in visited:
                        queue.append([next_point, path + [next_point]])
        return 'no path'

    def path_between_points_bfs_v3(self, points: List[dict], src: str, dst: str) -> str:
        graph = {point['name']: set(point['connections']) for point in points}
        if {src, dst}.issubset(graph):
            queue = [[src, [src]]]
            while len(queue) > 0:
                current_point, path = queue.pop(0)
                if current_point == dst:
                    return ' -> '.join(path)
                for next_point in graph[current_point]:
                    if next_point in graph:
                        queue.append([next_point, path + [next_point]])
                del graph[current_point]
        return 'no path'

    def path_between_points_bfs_v4(self, points: List[dict], src: str, dst: str) -> str:
        visited = {points[idx]['name']: idx for idx in range(0, len(points))}
        if {src, dst}.issubset(visited):
            src_idx, dst_idx = visited[src], visited[dst]
            queue = [[src_idx, [src]]]
            while len(queue) > 0:
                current_point_idx, path = queue.pop(0)
                if current_point_idx == dst_idx:
                    return ' -> '.join(path)
                for next_point in points[current_point_idx]['connections']:
                    if visited[next_point] != -1:
                        queue.append([visited[next_point], path + [next_point]])
                visited[points[current_point_idx]['name']] = -1
        return 'no path'
# ----------------------------------------------------------------------------------------------------------------------


examples = {
    ('A', 'F'): 'A -> B -> E -> F',
    ('D', 'B'): 'D -> C -> A -> B',
    ('A', 'B'): 'A -> B',
    ('D', 'F'): 'D -> C -> A -> B -> E -> F',
    ('D', 'G'): 'no path',
    ('Z', 'B'): 'no path',
    ('Z', 'S'): 'no path',
    ('A', 'H'): 'no path',
    ('G', 'H'): 'no path',
}

list_of_points = [
  {'name': "A", 'connections': ["B", "C", "G"]},
  {'name': "B", 'connections': ["A", "E"]},
  {'name': "C", 'connections': ["A", "D"]},
  {'name': "D", 'connections': ["C", "G"]},
  {'name': "E", 'connections': ["B", "F"]},
  {'name': "F", 'connections': ["E"]},
  {'name': "G", 'connections': []},
  {'name': "H", 'connections': []},
]

sol = Solution()
for ex in examples:
    print('dfs.....:\t%s = %s : %s' % (ex, examples[ex], sol.path_between_points_dfs(list_of_points, ex[0], ex[1])))
    print('bfs.....:\t%s = %s : %s' % (ex, examples[ex], sol.path_between_points_bfs(list_of_points, ex[0], ex[1])))
    print('bfs_v2..:\t%s = %s : %s' % (ex, examples[ex], sol.path_between_points_bfs_v2(list_of_points, ex[0], ex[1])))
    print('bfs_v3..:\t%s = %s : %s' % (ex, examples[ex], sol.path_between_points_bfs_v3(list_of_points, ex[0], ex[1])))
    print('bfs_v4..:\t%s = %s : %s' % (ex, examples[ex], sol.path_between_points_bfs_v4(list_of_points, ex[0], ex[1])))
    print()
# ----------------------------------------------------------------------------------------------------------------------
