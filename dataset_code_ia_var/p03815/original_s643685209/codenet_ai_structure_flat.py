x = int(input())
r = x % 11
q = x // 11
if r == 0:
    print(int(q * 2))
else:
    if 1 <= r <= 6:
        print(int(q * 2 + 1))
    else:
        print(int(q * 2 + 2))