N, R, T = map(int, input().split())
paces = [int(input()) for _ in range(N)]

# コンテナ補充タイミングは空に置いてから1単位時間後なので、
# 各給水所では容器の使用は1単位時間毎に循環している。
# 部員は毎単位時間必ず給水所で容器を受け取る必要があり、
# 各部員の位置（距離）に応じて必要な容器数が変わるため、
# 各単位時間で給水所に必要な容器数の最大値を求める。

# 給水所は周回コース長Rに沿っているため、
# 部員iのt単位時間目の位置は (p_i * t) % R
# これらの位置ごとの要求コンテナ数を記録し、
# ある単位時間における最大必要容器数を計算し、
# 最終的にT+1単位時間での最大値が最小必要容器数。

from collections import Counter

max_containers = 0
for t in range(T + 1):
    positions = [(paces[i] * t) % R for i in range(N)]
    counts = Counter(positions)
    max_containers = max(max_containers, max(counts.values()))

print(max_containers)