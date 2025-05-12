def power(x, n, d):
    rem = 1
    if n > 0:
        rem = power(x, n // 2, d)
        if n % 2 == 0:
            rem = rem ** 2 % d
        else:
            rem = ((rem ** 2 % d) * x) % d
    return rem

def solve():
    m, n = map(int, input().split())
    print(power(m, n, 1000000007))

solve()