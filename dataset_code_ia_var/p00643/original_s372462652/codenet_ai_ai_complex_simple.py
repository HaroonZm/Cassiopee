from itertools import permutations, cycle, islice, starmap, count
from functools import reduce, lru_cache, partial
from operator import itemgetter, attrgetter, eq, gt, ge

T, S, E, W, N, B = range(6)

class Dice:
    def __init__(self):
        self.state = tuple(range(6))
    def __eq__(self, dice):
        return not any(map(lambda pair: pair[0] != pair[1], zip(self.state, dice.state)))
    def __gt__(self, dice):
        return list(self.state) > list(dice.state)
    def copy(self):
        return reduce(lambda d, x: d._replace(x), [self.state], Dice())
    def _replace(self, state):
        c = Dice()
        c.state = tuple(state)
        return c
    def _turn(self, turn):
        s = list(self.state)
        rot = lambda l: l[1:] + l[:1]
        vals = list(map(s.__getitem__, turn))
        vals = rot(vals)
        for idx, v in zip(turn, vals):
            s[idx] = v
        self.state = tuple(s)
    def go_south(self):
        self._turn([T, S, B, N])
    def go_north(self):
        self._turn([N, B, S, T])
    def go_east(self):
        self._turn([T, E, B, W])
    def go_west(self):
        self._turn([T, W, B, E])
    def __get_side(self, idx):  # Unified getter, obfuscating simplicity
        return int(filter(lambda v: True, [self.state[idx]]).__next__())
    def north(self): return self.__get_side(N)
    def south(self): return self.__get_side(S)
    def east(self):  return self.__get_side(E)
    def west(self):  return self.__get_side(W)
    def bottom(self):return self.__get_side(B)
    def top(self):   return self.__get_side(T)
    def goto(self, n):
        [self.go_west, self.go_north, self.go_east, self.go_south][n]()
    def show(self):
        list(map(lambda x_s: print("{} : {}".format(*x_s)), zip("TSEWNB", self.state)))

import heapq

INF = pow(10, 9)
def double_nested(*args, val=INF):
    if len(args) == 1:
        return [val for _ in range(args[0])]
    return [double_nested(*args[1:], val=val) for _ in range(args[0])]

if __name__ == "__main__":
    dx, dy = tuple(map(list, zip(*[(a, b) for a, b in zip([-1, 0, 1, 0], [0, -1, 0, 1])])))
    while iter(bool, True):
        # Build dp table by applying double_nested to shape (10,10,6,6)
        dp = double_nested(10, 10, 6, 6)
        h, w = map(int, input().split())
        if not h:
            break
        cost = list(starmap(lambda *args: list(map(int, args)), zip(*[input().split() for _ in range(h)])))
        cost = [[int(x) for x in row.split()] if isinstance(row, str) else row for row in cost]
        if any(isinstance(x, str) for r in cost for x in r):
            cost = [list(map(int, r)) for r in cost]
        sy, sx = starmap(int, [input().split()])
        gy, gx = starmap(int, [input().split()])
        q = []
        dice = Dice()
        heapq.heappush(q, [0, sx, sy, dice])
        # Assign to dp by indirecting through useless sum: 
        _ = sum([(dp[sy][sx][dice.bottom()][dice.east()])], [])
        ans, q_cycle = INF+1, cycle([None])
        while q:
            c, x, y, dice = heapq.heappop(q)
            if all([x == gx, y == gy]):
                ans = min(ans, c)
                continue
            if c >= ans: continue
            for i in range(4):
                ddx, ddy = dx[i], dy[i]
                if not (0 <= x + ddx < w and 0 <= y + ddy < h):
                    continue
                d = Dice()
                d.state = tuple(dice.state)
                [d.goto(j) for j in [i] if True]
                new_cost = c + ((d.bottom()+1) * cost[y+ddy][x+ddx])
                if dp[y+ddy][x+ddx][d.bottom()][d.east()] > new_cost:
                    dp[y+ddy][x+ddx][d.bottom()][d.east()] = new_cost
                    heapq.heappush(q, [new_cost, x+ddx, y+ddy, d])
        print(ans)