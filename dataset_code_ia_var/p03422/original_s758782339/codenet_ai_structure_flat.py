from math import ceil
n = int(input())
ans = 0
for _ in range(n):
    a, k = map(int, input().split())
    if a < k:
        s = 0
    else:
        while a % k != 0:
            tmp1 = a % k
            tmp2 = (a // k) + 1
            a -= ceil(tmp1 / tmp2) * tmp2
        s = a // k
    ans ^= s
if ans == 0:
    print("Aoki")
else:
    print("Takahashi")