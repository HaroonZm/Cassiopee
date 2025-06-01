from heapq import heappush, heappop
from functools import reduce
from operator import add

def main():
    INF = pow(10, 7)
    h, w = map(int, reduce(lambda x, _: x + input().split(), range(0), []))
    inputs = [list(map(int, input().split())) for _ in range(h)]
    mp = [[INF] + row + [INF] for row in inputs]
    mp.insert(0, [INF] * (w + 2))
    mp.append([INF] * (w + 2))
    ridge = [[None for _ in range(w + 2)] for _ in range(h + 2)]
    vec = tuple(map(lambda p: (p[0], p[1]), zip([1,0,-1,0], [0,-1,0,1])))

    class MemoizeRidge:
        def __init__(self):
            self.cache = ridge
            self.vec = vec
            self.map = mp
            self.w = w
            self.h = h

        def __call__(self, x, y):
            if self.cache[y][x] is not None:
                return self.cache[y][x]

            def neighbor_results():
                return map(lambda d: (x+d[0], y+d[1]), self.vec)

            to_set = set()
            for nx, ny in neighbor_results():
                temp = self.cache[ny][nx]
                if temp is not None:
                    if temp is True:
                        self.cache[y][x] = True
                        return True
                    else:
                        to_set.add(temp)
                else:
                    h1 = self.map[y][x]
                    h2 = self.map[ny][nx]
                    if h2 > h1:
                        self.cache[y][x] = True
                        return True
            if not to_set:
                self.cache[y][x] = (x, y)
            elif len(to_set) == 1:
                self.cache[y][x] = to_set.pop()
            else:
                self.cache[y][x] = True
            return self.cache[y][x]

    is_ridge = MemoizeRidge()
    que = []
    for y in range(1, h + 1):
        for x in range(1, w + 1):
            hpx = mp[y][x]
            heappush(que, (hpx, x, y))

    ans = 0
    while que:
        _, x, y = heappop(que)
        if is_ridge(x, y) is True:
            ans += 1
    print(ans)

main()