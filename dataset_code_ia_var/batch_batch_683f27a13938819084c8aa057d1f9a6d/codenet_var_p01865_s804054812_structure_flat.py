n = int(input())
input()
s = 0
for _ in range(n):
    x, w = map(int, input().split())
    s += x * w
if s == 0:
    print(0)
else:
    if s > 0:
        print('1\n1', abs(s))
    else:
        print('1\n-1', abs(s))