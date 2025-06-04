import sys
sys.setrecursionlimit(10**7)

r,c,a1,a2,b1,b2 = map(int,input().split())

from collections import deque

mod = 100000007

dist = [[-1]*c for _ in range(r)]
count = [[0]*c for _ in range(r)]

dx = [1,-1,0,0]
dy = [0,0,1,-1]

dist[a1][a2] = 0
count[a1][a2] = 1

queue = deque()
queue.append((a1,a2))

while queue:
    x,y = queue.popleft()
    for i in range(4):
        nx = (x + dx[i]) % r
        ny = (y + dy[i]) % c
        if dist[nx][ny] == -1:
            dist[nx][ny] = dist[x][y] + 1
            count[nx][ny] = count[x][y]
            queue.append((nx,ny))
        elif dist[nx][ny] == dist[x][y] + 1:
            count[nx][ny] = (count[nx][ny] + count[x][y]) % mod

print(count[b1][b2] % mod)