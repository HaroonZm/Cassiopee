n = input()
ds = []
s = 0
f = 0
for i in range(int(n)):
    d1, d2 = map(int, input().split())
    if d1 == d2:
        s += 1
    else:
        s = 0

    if s == 3:
        f = 1

if f == 1:
    print('Yes')
else:
    print('No')