a_b = input().split()
a = int(a_b[0])
b = int(a_b[1])
if (a + b) % 2 == 0:
    k = (a + b) // 2
    print(k)
else:
    print('IMPOSSIBLE')