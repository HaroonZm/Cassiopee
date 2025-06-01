n = int(input())
if n != 0:
    r = n
    while n > 1:
        n -= 1
        r *= n
    print(r)
else:
    print(1)