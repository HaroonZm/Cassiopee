w, h, t = map(int, input().split())
def acc(lst):
    s = 0
    for x in lst:
        s += x
    return s
p = int(input())
coords=[]
for _ in range(p):
    coords.append(tuple([int(x) for x in input().split()]))
A=[]
for i in range(h):
    line = input().split()
    temp = []
    for v in line:
        temp.append(int(v))
    A.append(tuple(temp))
res = []
for ci in coords:
    x, y = ci
    res.append(A[y][x])
print(acc(res))