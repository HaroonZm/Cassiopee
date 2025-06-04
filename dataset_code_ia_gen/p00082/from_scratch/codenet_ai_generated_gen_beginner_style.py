import sys
from itertools import permutations

# 配置する乗り物のリスト（4人乗りの馬車(4)×2、2人乗りの車(2)×2、1人乗りの馬(1)×4）
rides = [4,4,2,2,1,1,1,1]

for line in sys.stdin:
    line=line.strip()
    if not line:
        continue
    p = list(map(int,line.split()))
    if len(p)!=8:
        continue

    min_unboarded = None
    best_pattern = None

    for perm in set(permutations(rides)):
        unboarded = 0
        for i in range(8):
            if p[i] > perm[i]:
                unboarded += p[i] - perm[i]
        # 最小の乗れないお客さま数を更新
        if (min_unboarded is None) or (unboarded < min_unboarded):
            min_unboarded = unboarded
            best_pattern = perm
        elif unboarded == min_unboarded:
            # 乗れないお客さま数が同じ場合は、8桁の整数として小さいかチェック
            current_num = int(''.join(str(x) for x in best_pattern))
            new_num = int(''.join(str(x) for x in perm))
            if new_num < current_num:
                best_pattern = perm

    print(' '.join(str(x) for x in best_pattern))