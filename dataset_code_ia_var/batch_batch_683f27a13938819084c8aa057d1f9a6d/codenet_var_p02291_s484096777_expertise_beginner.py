pp = list(map(int, input().split()))
n = int(input())

def length(v):
    s = 0
    for x in v:
        s += x*x
    return s ** 0.5

def dot(u, v):
    result = 0
    for x, y in zip(u, v):
        result += x * y
    return result

def project(point, p=pp):
    line_vec = (p[2] - p[0], p[3] - p[1])
    point_vec = (point[0] - p[0], point[1] - p[1])
    if dot(line_vec, point_vec) < 0:
        line_vec = (-line_vec[0], -line_vec[1])
    if length(line_vec) == 0:
        return [p[0], p[1]]
    t = dot(line_vec, point_vec) / (length(line_vec) ** 2)
    res = []
    for i in range(2):
        res.append(line_vec[i]*t + p[i])
    return res

def reflection(point, p=pp):
    proj = project(point, p)
    rx = point[0] + 2*(proj[0] - point[0])
    ry = point[1] + 2*(proj[1] - point[1])
    print(f"{rx:.8f} {ry:.8f}")

for _ in range(n):
    b = list(map(int, input().split()))
    reflection(b)