import sys
sys.setrecursionlimit(10**7)
N = int(input())
p = [0] + [int(input()) for _ in range(N)]

# 効果を適用して最終的に止まるマスを返す関数
def apply_effect(pos):
    visited = set()
    while p[pos] != 0:
        if pos in visited:
            # 無限ループ検出（入力条件よりゴール可能なのでここは使われないはず）
            break
        visited.add(pos)
        pos = pos + p[pos]
    return pos

from collections import deque
dist = [-1]*(N+1)
dist[1] = 0
queue = deque()
queue.append(1)

while queue:
    pos = queue.popleft()
    for dice in range(1,7):
        next_pos = pos + dice
        if next_pos >= N:
            # ゴールに到達したので出目はここで止められる
            print(dist[pos] + 1)
            sys.exit()
        next_pos = apply_effect(next_pos)
        if dist[next_pos] == -1:
            dist[next_pos] = dist[pos] + 1
            queue.append(next_pos)