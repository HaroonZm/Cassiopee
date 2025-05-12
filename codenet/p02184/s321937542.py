# 半分全列挙
from itertools import permutations, combinations
M = int(input())
C = list(map(int, input()))
if len(C)==1 and M==0:
    print(0)
    exit()
mod = 10**9 + 7
L = [0] * 10
b = 1
for c in C[::-1]:
    L[c] += b
    b = b * 10 % mod

for t_half1 in combinations(range(10), 5):
    L1, L2 = L[:5], L[5:]
    t_half2 = list(set(range(10)) - set(t_half1))
    if int(C[0]) < 5:
        s1 = {sum(l * n for l, n in zip(L1, t1)) % mod: t1 for t1 in reversed(list(permutations(t_half1))) if t1[int(C[0])] != 0}
    else:
        s1 = {sum(l * n for l, n in zip(L1, t1)) % mod: t1 for t1 in reversed(list(permutations(t_half1)))}
    for t2 in permutations(t_half2):
        s = sum(l * n for l, n in zip(L2, t2))
        if (M-s) % mod in s1:
            t = s1[(M-s) % mod] + t2
            if t[int(C[0])] != 0:
                print("".join(map(lambda x: str(t[x]), C)))
                exit()
print(-1)