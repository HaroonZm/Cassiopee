from heapq import heappush, heappop
from functools import lru_cache

def main():
    INF = float('inf')
    h, w = map(int, input().split())
    mp = [[INF, *map(int, input().split()), INF] for _ in range(h)]
    pad = [INF] * (w + 2)
    mp = [pad, *mp, pad]
    ridge = [[None] * (w + 2) for _ in range(h + 2)]
    directions = ((1, 0), (0, -1), (-1, 0), (0, 1))

    @lru_cache(maxsize=None)
    def is_ridge(x, y):
        to_set = set()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            nbr = ridge[ny][nx]
            if nbr is not None:
                if nbr is True:
                    ridge[y][x] = True
                    return True
                to_set.add(nbr)
        if not to_set:
            ridge[y][x] = (x, y)
        elif len(to_set) == 1:
            ridge[y][x] = next(iter(to_set))
        else:
            ridge[y][x] = True
        return ridge[y][x]

    hidx, widx = range(1, h + 1), range(1, w + 1)
    heap = [(mp[y][x], x, y) for y in hidx for x in widx]
    heap.sort()  # Faster than repeated heappush for static input

    ans = sum(is_ridge(x, y) is True for _, x, y in heap)
    print(ans)

main()