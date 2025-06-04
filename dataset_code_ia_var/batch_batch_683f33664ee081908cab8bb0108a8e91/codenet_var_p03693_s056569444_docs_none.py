x, y, z = input().split()
xyz = x + y + z
if int(xyz) % 4 == 0:
    print('YES')
else:
    print('NO')