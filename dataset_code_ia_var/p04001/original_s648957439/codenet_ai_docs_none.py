from itertools import product

S = input()
n = len(S)

ans = 0
for P in product(["+",""], repeat=n-1):
    res = ""
    for s, p in zip(S, P):
        res += s + p
    res += S[-1]
    ans += eval(res)
print(ans)