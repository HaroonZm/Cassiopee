from math import hypot
x1, y1, x2, y2 = map(int, input().split())
dx, dy = x2-x1, y2-y1
vector_a = hypot(dx, dy)
q = int(input())

for x3, y3 in (map(int, input().split()) for _ in [0]*q):
    d = ((x3-x1)*dx + (y3-y1)*dy) / (vector_a**2)
    print(x1+dx*d, y1+dy*d)