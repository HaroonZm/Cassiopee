n = int(input())
a, b = map(int, input().split())
c, d = map(int, input().split())
a -= 1
b -= 1
c -= 1
d -= 1
res = None
for i in range(n):
    z = i + 1
    x1, y1 = a, b
    x2, y2 = c, d
    f1 = abs(x1 // z - y1 // z) + abs(x1 % z - y1 % z)
    f2 = abs(x2 // z - y2 // z) + abs(x2 % z - y2 % z)
    s = f1 + f2
    if res is None or s < res:
        res = s
print(res)