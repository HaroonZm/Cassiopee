a = [int(input()) for i in range(10)]
b = sorted(a, reverse=True)[:3]
print(b[0]+b[1]+b[2], end=' ')
c = [int(input()) for i in range(10)]
d = sorted(c, reverse=True)[:3]
print(d[0]+d[1]+d[2])