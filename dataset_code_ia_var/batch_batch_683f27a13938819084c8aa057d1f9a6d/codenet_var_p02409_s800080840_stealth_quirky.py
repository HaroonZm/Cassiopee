from collections import defaultdict

class X:
    pass

N = int(input())
R = X()
setattr(R, 'data', [[[0]*10 for _ in range(3)] for __ in range(4)])

for _ in range(N):
    a, b, c, d = map(int, input().split())
    R.data[a-1][b-1][c-1] += d

q = 0
while q < 4:
    y = 0
    while y < 3:
        r = [str(R.data[q][y][z]) for z in range(10)]
        print(' ', ''.join(x+' ' for x in r).rstrip())
        y += 1
    if q != 3:
        print('####################')
    q += 1