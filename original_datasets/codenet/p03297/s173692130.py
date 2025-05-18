T = int(input())
def gcd(m, n):
    r = m % n
    return gcd(n, r) if r else n
def check(a, b, c, d):
    if b > a or d < b:
        return 0
    g = gcd(b, d)
    k = (a - c - 1) // g
    p = a - k*g
    if p - b < 0:
        return 0
    return 1

for _ in range(T):
    a, b, c, d = map(int, input().split())
    print("Yes" if check(a, b, c, d) else "No")