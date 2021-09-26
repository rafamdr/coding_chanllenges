# You’re trying to build an IoT mesh network. Signals can only travel the maximum of 5 units. You’re given coordinates
# for the switch, the light, and the mesh hubs (which capture and forward signals). Return true if the switch can
# successfully toggle the light.
#
# Example:
# let network = { switch: [0,1], hub: [[2,1], [2,5]], light: [1,6] }
# $ canToggle(network)
# $ true
# ----------------------------------------------------------------------------------------------------------------------


import math
from typing import Tuple
from collections import deque
import turtle
# ----------------------------------------------------------------------------------------------------------------------


class Mesh:
    def __init__(self, switch: Tuple[int, int], hub: Tuple[Tuple[int, int], ...], light: Tuple[int, int]):
        self.switch = switch
        self.hub = hub
        self.light = light

    def __hash__(self):
        return hash((self.switch, self.hub, self.light))

    def __eq__(self, other):
        return (self.switch, self.hub, self.light) == (other.switch, other.hub, other.light)
# ----------------------------------------------------------------------------------------------------------------------


class Solution:
    def _euclid_dist(self, v1: Tuple[int, int], v2: Tuple[int, int]) -> float:
        return math.sqrt(((v1[0] - v2[0]) ** 2) + ((v1[1] - v2[1]) ** 2))

    def can_toggle_ref(self, mesh: Mesh, max_dist=5) -> bool:
        graph = {'switch': {}, 'light': {}}
        for i, h in enumerate(mesh.hub):
            graph['h%d' % i] = {}
            if (temp_d := self._euclid_dist(mesh.switch, h)) <= max_dist:
                graph['switch']['h%d' % i] = temp_d
            if (temp_d := self._euclid_dist(mesh.light, h)) <= max_dist:
                graph['h%d' % i]['light'] = temp_d
            for j, ht in enumerate(mesh.hub):
                if h != ht and (temp_d := self._euclid_dist(h, ht)) <= max_dist:
                    graph['h%d' % i]['h%d' % j] = temp_d
        queue = deque(['switch'])
        visited = {'switch'}
        while len(queue) > 0:
            v = queue.pop()
            for e in graph[v]:
                if e not in visited:
                    if e == 'light':
                        return True
                    queue.append(e)
                    visited.add(e)
        return False

    def can_toggle_ref2(self, mesh: Mesh, max_dist=5) -> bool:
        queue = deque()
        visited = {-1}
        for i, h in enumerate(mesh.hub):
            if self._euclid_dist(mesh.switch, h) <= max_dist:
                queue.append(i)
        while len(queue) > 0:
            v = mesh.hub[queue.pop()]
            if self._euclid_dist(mesh.light, v) <= max_dist:
                return True
            for i, h in enumerate(mesh.hub):
                if (v != h) and (i not in visited) and self._euclid_dist(v, h) <= max_dist:
                    queue.append(i)
                    visited.add(i)
        return False

    def _check_dist(self, v1: Tuple[int, int], v2: Tuple[int, int], dist) -> bool:
        dx = v1[0] - v2[0]
        dy = v1[1] - v2[1]
        return (dx * dx) + (dy * dy) <= (dist * dist)

    def can_toggle_improved(self, mesh: Mesh, max_dist=5) -> bool:
        queue = deque()
        visited = [0] * len(mesh.hub)
        for i, h in enumerate(mesh.hub):
            if self._check_dist(mesh.switch, h, max_dist):
                queue.append(i)
        while len(queue) > 0:
            v = mesh.hub[queue.pop()]
            if self._check_dist(mesh.light, v, max_dist):
                return True
            for i, h in enumerate(mesh.hub):
                if (v != h) and (visited[i] == 0) and self._check_dist(v, h, max_dist):
                    queue.append(i)
                    visited[i] = 1
        return False
# ----------------------------------------------------------------------------------------------------------------------


examples = {
    Mesh(switch=(0, 1), hub=((1, 1),), light=(1, 5)): True,
    Mesh(switch=(0, 1), hub=((2, 1), (2, 5)), light=(1, 6)): True,
    Mesh(switch=(0, 1), hub=((2, 1), (3, 3), (2, 5)), light=(1, 6)): True,
    Mesh(switch=(0, 1), hub=((2, 1), (3, 3)), light=(100, 60)): False,
    Mesh(switch=(0, 0), hub=((0, 5), (0, 10), (0, 15), (2, 17)), light=(0, 21)): True,
    Mesh(switch=(0, 0), hub=(
        (0, 5), (0, 10), (0, 15), (0, 20), (0, 25),
        (5, 15), (10, 15), (15, 15), (20, 15), (20, 20),
        (20, 25), (20, 30), (20, 35), (20, 40), (15, 40),
        (10, 40), (5, 40),
    ), light=(0, 40)): True,
}
DRAW_SOMETHING = False
MAX_RADIUS = 5
ZOOM = 5
if DRAW_SOMETHING:
    drawer = turtle.Turtle()
    drawer.getscreen().delay(0)
    drawer.hideturtle()


def draw_circle_tuple(drawer: turtle.Turtle, t: Tuple[int, int], max_radius, zoom, color: str):
    drawer.color(color)
    drawer.penup()
    drawer.goto(t[0] * zoom, t[1] * zoom)
    drawer.pendown()
    drawer.circle(max_radius * zoom)


def draw_mesh(drawer: turtle.Turtle, mesh: Mesh, max_radius, zoom):
    drawer.clear()
    draw_circle_tuple(drawer, mesh.switch, max_radius, zoom, 'red')
    for h in mesh.hub:
        draw_circle_tuple(drawer, h, max_radius, zoom, 'black')
    draw_circle_tuple(drawer, mesh.light, max_radius, zoom, 'blue')

sol = Solution()
for ex in examples:
    if DRAW_SOMETHING:
        draw_mesh(drawer, ex, MAX_RADIUS, ZOOM)
    print('Ref...: %s -> %s : %s' % (str(ex), sol.can_toggle_ref(ex), str(examples[ex])))
    print('Ref2..: %s -> %s : %s' % (str(ex), sol.can_toggle_ref2(ex), str(examples[ex])))
    print('Improv: %s -> %s : %s' % (str(ex), sol.can_toggle_improved(ex), str(examples[ex])))
    print()
# ----------------------------------------------------------------------------------------------------------------------
