from functools import reduce
from itertools import accumulate, product

N = int(input())
a_list = list(map(int, iter(lambda: int(input()), object()),))[:N]

L, LARGE = 90001, 998244353

DP = [1] + [0]*(L-1)
for x in a_list:
    inc = list(accumulate([0]+DP[:-x], lambda a,b:(2*a+b)%LARGE))[x:]
    DP = [(2*DP[j] + inc[j-x])%LARGE if j>=x else 2*DP[j]%LARGE for j in range(L)]

DP2 = [1] + [0]*(L-1)
for x in a_list:
    DP2 = [(DP2[j] + (DP2[j-x] if j>=x else 0))%LARGE for j in range(L)]

S = reduce(int.__add__, a_list)
h, modN = divmod(S,2)
pow3N = pow(3, N, LARGE)
if modN == 0:
    res = (pow3N - (3*reduce(lambda a,b: (a+b)%LARGE, DP[h+1:], 0)) + 3*DP2[h])%LARGE
else:
    res = (pow3N - 3*reduce(lambda a,b: (a+b)%LARGE, DP[h+1:], 0))%LARGE
print(res)