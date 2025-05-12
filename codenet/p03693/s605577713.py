r, g, b = [int(n) for n in input().split()]

if (10*g+b) % 4 == 0:
    print('YES')
else:
    print('NO')