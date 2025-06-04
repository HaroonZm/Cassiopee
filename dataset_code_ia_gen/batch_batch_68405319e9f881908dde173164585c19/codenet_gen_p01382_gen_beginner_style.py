N = int(input())
a = []
for _ in range(N):
    a.append(int(input()))

a.sort(reverse=True)

def can_make_triangle(x, y, z):
    return x < y + z and y < x + z and z < x + y

max_perimeter = 0
found = False

# 選ぶ6本の棒の組み合わせ全部を調べる（非効率だが簡単な方法）
from itertools import combinations, permutations

for six_sticks in combinations(a, 6):
    # 6本の棒を2つの三角形の3本ずつに分ける方法を全探索
    # 6本の棒の順列を考えて、前3本と後3本を三角形にする
    for perm in permutations(six_sticks):
        tri1 = perm[0:3]
        tri2 = perm[3:6]
        if can_make_triangle(*tri1) and can_make_triangle(*tri2):
            p = sum(tri1) + sum(tri2)
            if p > max_perimeter:
                max_perimeter = p
                found = True

if found:
    print(max_perimeter)
else:
    print(0)