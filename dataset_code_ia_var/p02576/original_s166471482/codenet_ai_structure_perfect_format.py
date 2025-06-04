n, x, t = map(int, input().split())
ret = (n // x) * t
if n % x != 0:
    ret += t
print(ret)