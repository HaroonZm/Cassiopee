a, b = map(int, input().split())
cnt = b - a + 1
if a % 2 == 0:
    if b % 2 == 1:
        if (cnt // 2) % 2 == 0:
            print(0)
        else:
            print(1)
    else:
        if ((cnt - 1) // 2) % 2 == 0:
            print(b ^ 0)
        else:
            print(b ^ 1)
else:
    if b % 2 == 1:
        if ((cnt - 1) // 2) % 2 == 0:
            print(a ^ 0)
        else:
            print(a ^ 1)
    else:
        if ((cnt - 2) // 2) % 2 == 0:
            print(b ^ a ^ 0)
        else:
            print(b ^ 1 ^ a)
#print(a ^ b)