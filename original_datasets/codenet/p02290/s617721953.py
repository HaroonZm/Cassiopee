from math import hypot

x1, y1, x2, y2 = map(int, input().split())
dx, dy = x2-x1, y2-y1
vector_base = hypot(dx, dy)
q = int(input())

for i in range(q):
    x3, y3 = map(int, input().split()) 
    d = ((x3-x1)*dx + (y3-y1)*dy) / (vector_base**2)
    print(x1+dx*d, y1+dy*d)