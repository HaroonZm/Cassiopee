input()
m = int(input())
s = 0
for _ in range(m):
    x, w = map(int, input().split())
    s += x * w
if s:
    if s > 0:
        print('1\n1 %d' % abs(s))
    else:
        print('1\n-1 %d' % abs(s))
else:
    print(0)