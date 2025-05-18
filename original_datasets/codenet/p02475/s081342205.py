a, b = map(int,input().split())
sign = 1 if (a < 0) == (b < 0) else -1
a = abs(a)
b = abs(b)
print((a // b) * sign)