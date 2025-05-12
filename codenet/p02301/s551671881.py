def diff(i):
    cp, np = points[i:i + 2]
    return np - cp

def cross(a, b):
    return a.real * b.imag - a.imag * b.real

def diameter(i, j):
    return abs(points[i] - points[j])

n = int(input())
t_points = [tuple(map(float, input().split())) for _ in range(n)]
i = min(range(n), key=lambda x: t_points[x])
j = max(range(n), key=lambda x: t_points[x])
points = [re + 1j * im for re, im in t_points]
points.append(points[0])
tentative_diameter = diameter(i, j)

it, jt = i, j
while True:
    if cross(diff(it), diff(jt)) >= 0:
        jt = (jt + 1) % n
    else:
        it = (it + 1) % n
    tentative_diameter = max(tentative_diameter, diameter(it, jt))

    if it == i and jt == j:
        break

print(tentative_diameter)