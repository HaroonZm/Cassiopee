s = int(input())
mod = 10 ** 9 + 7

ans = 0
for l in range(1, 1000):
    ss = s - 2 * l - 1
    if ss < 0:
        continue
    comb = 1
    for i in range(l - 1):
        comb *= ss - i
        comb //= i + 1

    ans += comb
    ans %= mod

print(ans)