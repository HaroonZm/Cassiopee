#!/bin/env python
import sys
import heapq
from collections import defaultdict, deque

class Grid:
    '''
    Grid provide 2 dim axis search for grid.
    '''
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
        '''
        Removes switch recursivery, that only one switch exists in line.
        But leaves switch in line on START.
        '''
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
            # But reaves switch in line on START.
            if sw[0] == 1 or sw == self.goal:
                continue
            self.remove(sw)
            next_dir = (direction + 1) % 2
            q.append((next_dir, sw[next_dir]))

    def has_route(self):
        '''
        If no switches exists in goal line, it never can goal.
        '''
        return len(self.by_d[0][self.goal[0]]) > 1 \
            or len(self.by_d[1][self.goal[1]]) > 1

    def get_sameline_switch(self, direction, sw):
        return (s for s in self.get_points(direction, sw[direction])
                if s != sw)

class Searcher:
    def __init__(self, grid):
        self.grid = grid
        self.q = []
        self.best_time = {}
        self.deadline = {0: set(), 1: set()}

    def next_depth(self, t, current, direction):
        # ゴールであれば、ゴールの時間を返し終了
        if current == self.grid.goal:
            return t - 1  # remove last switch push time.

        # 該当行が、既に全探索済みであれば、打ち切り
        if current[direction] in self.deadline[direction]:
            return

        next_dir = (direction + 1) % 2

        has_next_switch = False
        for sw in self.grid.get_sameline_switch(direction, current):
            # sw での時間は、現在の時間(t) + 距離 + スイッチ押下(1)
            next_t = t + abs(sw[next_dir] - current[next_dir]) + 1
            best_t = self.best_time.get(sw, float('inf'))
            if best_t <= next_t:
                continue
            # swへの最短経路を発見
            self.best_time[sw] = next_t
            heapq.heappush(self.q, (next_t, sw, next_dir))
            has_next_switch = True

        # 1つもbest time となるスイッチがなければ、その行自体NG
        if not has_next_switch:
            self.deadline[direction].add(current[direction])

    def search(self):
        ''' Returns all "time" '''
        # 最初に、duration:0 方向にしか移動できないというルールを、
        # (1, 0)から始めることで実現
        self.q.append((0, (1, 0), 0))
        while self.q:
            res = self.next_depth(*heapq.heappop(self.q))
            if res:
                yield res - 1  # remove first move (1, 0) to (1, 1)

    def search_one(self):
        ''' returns best or -1 '''
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