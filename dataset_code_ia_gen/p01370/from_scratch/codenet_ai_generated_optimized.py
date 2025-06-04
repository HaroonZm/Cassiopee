import sys
sys.setrecursionlimit(10**7)

# 隣接6方向の相対座標
dirs = [(1,0),(0,1),(-1,1),(-1,0),(0,-1),(1,-1)]

def bfs(t, obstacles, start):
    from collections import deque
    visited = set()
    visited.add(start)
    queue = deque()
    queue.append((start[0], start[1], 0))
    while queue:
        x, y, d = queue.popleft()
        if d == t:
            continue
        for dx, dy in dirs:
            nx, ny = x+dx, y+dy
            if (nx, ny) not in obstacles and (nx, ny) not in visited and -30 <= nx <= 30 and -30 <= ny <= 30:
                visited.add((nx, ny))
                queue.append((nx, ny, d+1))
    return len(visited)

def main():
    import sys
    input = sys.stdin.readline
    while True:
        line = input()
        if not line:
            break
        t, n = map(int, line.split())
        if t == 0 and n == 0:
            break
        obstacles = set()
        for _ in range(n):
            x, y = map(int, input().split())
            obstacles.add((x, y))
        sx, sy = map(int, input().split())
        print(bfs(t, obstacles, (sx, sy)))

if __name__=="__main__":
    main()