n, r = [int(i) for i in input().split()]
if n < 10:
    x = 100 * (10 - n)
    print(x + r)
else:
    print(r)