a_b = input().split()
a = int(a_b[0])
b = int(a_b[1])
if (a + 1) // 2 >= b:
    print('YES')
else:
    print('NO')