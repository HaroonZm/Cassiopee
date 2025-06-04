from sys import stdin

def sign(p1, p2, p3):
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3
    return (x1 - x3) * (y2 - y3) - (x2 - x3) * (y1 - y3)

def check(triangle, pt):
    v1 = triangle[0:2]
    v2 = triangle[2:4]
    v3 = triangle[4:6]
    s1 = sign(pt, v1, v2)
    s2 = sign(pt, v2, v3)
    s3 = sign(pt, v3, v1)
    pos = lambda x: x > 0
    # All positive or all non-positive
    return (pos(s1) == pos(s2) == pos(s3))

n = int(stdin.readline())

for _ in range(n):
    query = list(map(int, stdin.readline().split()))
    triangle = query[:6]
    hikoboshi, orihime = query[6:8], query[8:10]
    res = check(triangle, hikoboshi) ^ check(triangle, orihime)
    print('OK' if res else 'NG')