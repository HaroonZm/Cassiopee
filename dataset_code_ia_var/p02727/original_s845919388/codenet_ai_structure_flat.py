x, y, a, b, c = list(map(int, input().split()))
p = list(map(int, input().split()))
q = list(map(int, input().split()))
r = list(map(int, input().split()))
p.sort()
q.sort()
tmp1 = []
for i in range(a-x, a):
    tmp1.append(p[i])
for i in range(b-y, b):
    tmp1.append(q[i])
for i in range(c):
    tmp1.append(r[i])
tmp1.sort()
s = 0
for i in range(x+y):
    s += tmp1[-(i+1)]
print(s)