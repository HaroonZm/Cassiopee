import sys
sys.setrecursionlimit(10**7)
from math import isclose

W,H=map(int,input().split())
maze=[list(input()) for _ in range(H)]

floor=[]
spring=[]
dist=[[float('inf')]*W for _ in range(H)]
for y in range(H):
    for x in range(W):
        if maze[y][x] in '.sg':
            floor.append((y,x))
        if maze[y][x]=='*':
            spring.append((y,x))
        if maze[y][x]=='s':
            sy,sx=y,x
        if maze[y][x]=='g':
            gy,gx=y,x

floor_set=set(floor)
spring_set=set(spring)

dx=[1,-1,0,0]
dy=[0,0,1,-1]

# ベースはゴールからの距離を BFS で計算
from collections import deque
q=deque()
dist_goal=[[float('inf')]*W for _ in range(H)]
dist_goal[gy][gx]=0
q.append((gy,gx))
while q:
    y,x=q.popleft()
    for i in range(4):
        ny,nx=y+dy[i],x+dx[i]
        if 0<=ny<H and 0<=nx<W and maze[ny][nx]!='#':
            if dist_goal[ny][nx]>dist_goal[y][x]+1:
                dist_goal[ny][nx]=dist_goal[y][x]+1
                q.append((ny,nx))

# 期待値計算
# E(s)= min over neighbors(v) of 1 + E(v), v is floor or goal tile
# if s is spring:
# E(s) = average over all floor tiles f of E(f)

# 全ての床タイルの期待値を求める
# springで飛ばされるので，飛ばされ時の期待値は floor全体の平均となる。

# 期待値を初期化
E=[[float('inf')]*W for _ in range(H)]
for y,x in floor:
    E[y][x]=dist_goal[y][x]
for y,x in spring:
    E[y][x]=0.0

floor_tiles = floor
floor_count = len(floor_tiles)

threshold=1e-12

while True:
    updated=False

    # springの期待値は平均
    spring_E_sum=0.0
    for y,x in floor_tiles:
        spring_E_sum+=E[y][x]
    spring_E_avg=spring_E_sum/floor_count

    for y,x in spring:
        if not isclose(E[y][x],spring_E_avg,abs_tol=threshold):
            E[y][x]=spring_E_avg
            updated=True

    # floorの期待値はmin(1+隣接の期待値)
    for y,x in floor_tiles:
        if maze[y][x]=='g':
            continue
        old=E[y][x]
        cand=[]
        for i in range(4):
            ny,nx=y+dy[i],x+dx[i]
            if 0<=ny<H and 0<=nx<W and maze[ny][nx]!='#':
                if maze[ny][nx]=='*':
                    # springに乗ったら飛ばされる
                    # springのEは平均値なのでそのまま使える
                    cand.append(1+E[ny][nx])
                else:
                    cand.append(1+E[ny][nx])
        if cand:
            val=min(cand)
            if abs(E[y][x]-val)>threshold:
                E[y][x]=val
                updated=True
    if not updated:
        break

print(f"{E[sy][sx]:.12f}")