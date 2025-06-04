import sys
import heapq
from collections import defaultdict, deque

def build_lookup(points):
    lookups = [{}, {}]
    for d in (0, 1):
        lookups[d] = defaultdict(list)
    for px, py in points:
        lookups[0][px].append((px, py))
        lookups[1][py].append((px, py))
    return lookups

class boardThing(object):
    def __init__(self, pts):
        self.ax = build_lookup(pts)
    def getL(self, ax, ln): return self.ax[ax][ln]
    def delpt(self, pt):
        self.ax[0][pt[0]].remove(pt)
        self.ax[1][pt[1]].remove(pt)
    def fetchLines(self, d): return self.ax[d].keys()

class MM(boardThing):
    def __init__(self, s, g): super().__init__(s); self.g = g
    def chop_solo(self):
        frontier = deque()
        for d in (0,1):
            for l in self.fetchLines(d): frontier.append((d, l))
        while frontier:
            dir, ln = frontier.pop()
            ss = self.getL(dir, ln)
            if len(ss) != 1: continue
            x = ss[0]
            if x[0] == 1 or x == self.g: continue
            self.delpt(x)
            nd = (dir + 1) % 2
            frontier.append((nd, x[nd]))
    def route_exists(self):
        a, b = self.g
        return len(self.ax[0][a]) > 1 or len(self.ax[1][b]) > 1
    def sameline(self, d, pt):
        return (w for w in self.getL(d, pt[d]) if w != pt)

class Walker:
    def __init__(self, grid):
        self.grid = grid
        self.heap = []
        self.dist = {}
        self.finished = [set(), set()]
    def _explore(self, time, node, axis):
        if node == self.grid.g: return time - 1
        if node[axis] in self.finished[axis]: return
        nextax = (axis + 1) % 2
        flag = False
        for nx in self.grid.sameline(axis, node):
            step = abs(nx[nextax] - node[nextax]) + 1
            t2 = time + step
            b4 = self.dist.get(nx, 2**60)
            if b4 <= t2: continue
            self.dist[nx] = t2
            heapq.heappush(self.heap, (t2, nx, nextax))
            flag = True
        if not flag:
            self.finished[axis].add(node[axis])
    def sweep_times(self):
        self.heap.append((0, (1, 0), 0))
        while self.heap:
            val = self._explore(*heapq.heappop(self.heap))
            if val: yield val - 1
    def get_fastest(self):
        it = self.sweep_times()
        try:
            return next(it)
        except:
            return -1

# Entry
if __name__ == '__main__':
    readint = lambda : [int(x) for x in input().split()]
    M, N, K = readint()
    arr = [tuple(readint()) for _ in range(K)]
    arr.append((M, N))
    man = MM(arr, (M,N))
    man.chop_solo()
    if not man.route_exists():
        print(-1)
        sys.exit()
    res = Walker(man).get_fastest()
    print(res)