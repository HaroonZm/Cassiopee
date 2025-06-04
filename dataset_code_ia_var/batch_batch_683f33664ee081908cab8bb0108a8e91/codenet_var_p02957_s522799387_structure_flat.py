a, b = map(int, input().split())
s = a + b
if s % 2 == 0:
    m = s // 2
    print(m)
else:
    print('IMPOSSIBLE')