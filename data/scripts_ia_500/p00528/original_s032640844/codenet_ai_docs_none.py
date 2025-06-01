#!/bin/env python
import sys
import heapq
from collections import defaultdict, deque

class Grid:
    def __init__(self, points):
        self.by_d = {0: defaultdict(list), 1: defaultdict(list)}
        for x, y in points:
            self.by_d[0][x].append((x, y))
            self.by_d[1][y].append((x, y))

    def get_points(self, axis, line_no):
        return self.by_d[axis][line_no]

    def remove(self, point):
        self.by_d[0][point[0]].remove(point)
        self.by_d[1][point[1]].remove(point)

    def get_lines(self, direction):
        return self.by_d[direction].keys()

class ModernMansion(Grid):
    def __init__(self, switches, goal):
        super().__init__(switches)
        self.goal = goal

    def remove_orphan(self):
        q = deque()
        for direction in (0, 1):
            for line in self.get_lines(direction):
                q.append((direction, line))
        while q:
            direction, line = q.pop()
            switches = self.get_points(direction, line)
            if len(switches) != 1:
                continue
            sw = switches[0]
            if sw[0] == 1 or sw == self.goal:
                continue
            self.remove(sw)
            next_dir = (direction + 1) % 2
            q.append((next_dir, sw[next_dir]))

    def has_route(self):
        return len(self.by_d[0][self.goal[0]]) > 1 or len(self.by_d[1][self.goal[1]]) > 1

    def get_sameline_switch(self, direction, sw):
        return (s for s in self.get_points(direction, sw[direction]) if s != sw)

class Searcher:
    def __init__(self, grid):
        self.grid = grid
        self.q = []
        self.best_time = {}
        self.deadline = {0: set(), 1: set()}

    def next_depth(self, t, current, direction):
        if current == self.grid.goal:
            return t - 1
        if current[direction] in self.deadline[direction]:
            return
        next_dir = (direction + 1) % 2
        has_next_switch = False
        for sw in self.grid.get_sameline_switch(direction, current):
            next_t = t + abs(sw[next_dir] - current[next_dir]) + 1
            best_t = self.best_time.get(sw, float('inf'))
            if best_t <= next_t:
                continue
            self.best_time[sw] = next_t
            heapq.heappush(self.q, (next_t, sw, next_dir))
            has_next_switch = True
        if not has_next_switch:
            self.deadline[direction].add(current[direction])

    def search(self):
        self.q.append((0, (1, 0), 0))
        while self.q:
            res = self.next_depth(*heapq.heappop(self.q))
            if res:
                yield res - 1

    def search_one(self):
        try:
            return next(self.search())
        except StopIteration:
            return -1

if __name__ == '__main__':
    M, N, K = map(int, input().split())
    switches = [tuple(map(int, input().split())) for _ in range(K)]
    switches.append((M, N))
    grid = ModernMansion(switches, (M, N))
    grid.remove_orphan()
    if not grid.has_route():
        print('-1')
        sys.exit()
    searcher = Searcher(grid)
    res = searcher.search_one()
    print(res)