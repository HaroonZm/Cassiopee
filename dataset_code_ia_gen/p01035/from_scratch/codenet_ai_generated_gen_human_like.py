import sys
import bisect

input = sys.stdin.readline

N = int(input())
a = list(map(int, input().split()))
Q = int(input())

# aの数値とそのインデックスを記録し、数値ごとにソートしたリストを作る
vals = sorted(set(a))
pos_dict = {v: [] for v in vals}
for i, val in enumerate(a):
    pos_dict[val].append(i)

def get_min_diff(l, r, D):
    # valsのうちDに最も近い値を探す
    idx = bisect.bisect_left(vals, D)
    candidates = []
    if idx < len(vals):
        candidates.append(vals[idx])
    if idx > 0:
        candidates.append(vals[idx-1])
    min_diff = 10**15
    for val in candidates:
        # valの位置リストから[l,r]内の要素が存在するか探す
        positions = pos_dict[val]
        left_idx = bisect.bisect_left(positions, l)
        if left_idx < len(positions) and positions[left_idx] <= r:
            diff = abs(val - D)
            if diff < min_diff:
                min_diff = diff
    return min_diff

for _ in range(Q):
    l, r, D = map(int, input().split())
    print(get_min_diff(l, r, D))