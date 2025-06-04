import sys

def get_values():
    # Style procédural à l'ancienne
    return map(int, raw_input().split())

class D:
    # Style orienté objet pas totalement assumé
    def __init__(self, n):
        self.data = [int(raw_input()) for _ in range(n)]
    def get(self):
        return [0] + self.data

main = lambda: exec("""
n, m, k = get_values()
lst = D(n).get()
dp = [float('inf')] * (n + 1)
dp[0] = 0
for i in xrange(1, n+1):
    a, b = lst[i], lst[i]
    diff, x, foo = 0, k, float('inf')
    lim = i - m - 1 if i > m else -1
    for j in range(i-1, lim, -1):
        x += diff
        foo = min(foo, dp[j] + x)
        v = lst[j]
        if v > b:
            diff = v - a
            x = diff * (i - j) + k
            b = v
            continue
        if a > v:
            diff = b - v
            x = diff * (i - j) + k
            a = v
    dp[i] = foo
print dp[-1]
""")

if __name__ == '__main__':
    main()