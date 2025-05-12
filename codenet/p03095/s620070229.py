from collections import Counter

MOD = 10 ** 9 + 7
input()
S = input()
ans = 1
for v in Counter(S).values():
    ans *= v + 1
    ans %= MOD
print(ans - 1)