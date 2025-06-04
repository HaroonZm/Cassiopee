n = int(input())
a = list(map(int, input().split()))

# Terrain heights with sentinels at both ends set to -1 (below sea level)
h = [-1] + a + [-1]

is_land = [False] * (n+2)  # Track if each section is currently land
is_island = [False] * (n+2) # Track if section is start of an island

island_count = 0
max_island_count = 0

def is_start_of_island(i):
    # i番地が島の始まりか判定（i番地が陸地で且つi-1が陸地でない）
    return is_land[i] and not is_land[i-1]

# 初期状態（海面高さ0）の島の個数を計算
for i in range(1, n+1):
    if h[i] > 0:
        is_land[i] = True

for i in range(1, n+1):
    is_island[i] = is_start_of_island(i)
    if is_island[i]:
        island_count += 1

max_island_count = island_count

# 高さごとに区画をまとめる
from collections import defaultdict
height_positions = defaultdict(list)
for i in range(1, n+1):
    height_positions[h[i]].append(i)

# 高さを昇順にして海面の高さが上がるごとに陸地が沈む処理
for height in sorted(height_positions):
    # 海面がheightになり、h[i] == height の区画が沈む
    for i in height_positions[height]:
        if is_land[i]:
            # i番地が陸地から海へ変わるので、まず島の始まりかチェックして島の数を調整
            if is_start_of_island(i):
                island_count -= 1
                is_island[i] = False
            # i番地つぶす
            is_land[i] = False
            # i+1が陸地になっていればそのi+1は島の始まりかもしれないので更新
            if i+1 <= n:
                was_start = is_island[i+1]
                now_start = is_start_of_island(i+1)
                if was_start and not now_start:
                    island_count -= 1
                    is_island[i+1] = False
                elif not was_start and now_start:
                    island_count += 1
                    is_island[i+1] = True
            # i-1が陸地になっていればそのi-1は島の始まりかもしれないが、
            # i-1 については島の始まり判定は i-1 で行うためここでは不要
            # (i-1 の島の始まりはi-1番地の位置で判定される)
    if island_count > max_island_count:
        max_island_count = island_count

print(max_island_count)