from heapq import heappush, heappop
from sys import stdin, setrecursionlimit

setrecursionlimit(10**7)
input = stdin.readline

def main():
    INF = 10**7
    h, w = map(int, input().split())
    mp = [[INF] * (w + 2)] + [[INF] + list(map(int, input().split())) + [INF] for _ in range(h)] + [[INF] * (w + 2)]
    ridge = [[None] * (w + 2) for _ in range(h + 2)]
    directions = [(1, 0), (0, -1), (-1, 0), (0, 1)]
    
    def is_ridge(x, y):
        if ridge[y][x] is not None:
            return ridge[y][x]
        
        neighbors = set()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            temp = is_ridge(nx, ny)
            if temp is True:
                ridge[y][x] = True
                return True
            neighbors.add(temp)
        
        neighbors.discard(None)
        if not neighbors:
            ridge[y][x] = (x, y)
        elif len(neighbors) == 1:
            ridge[y][x] = neighbors.pop()
        else:
            ridge[y][x] = True
        return ridge[y][x]
    
    heap = []
    for y in range(1, h + 1):
        row = mp[y]
        for x in range(1, w + 1):
            heappush(heap, (row[x], x, y))
    
    ans = sum(is_ridge(x, y) is True for _, x, y in iter(heappop, None) if heap)
    
    # Because iter(heappop, None) is invalid, rewrite while loop optimally:
    ans = 0
    while heap:
        _, x, y = heappop(heap)
        if is_ridge(x, y) is True:
            ans += 1

    print(ans)

main()