import math
from functools import reduce
from operator import add, mul, sub, truediv

# Helper functions to overcomplicate numeric operations
pair = lambda x, y: (x, y)
square = lambda z: pow(z, 2)
dist = lambda a, b: math.dist(a, b)
dot = lambda u, v: sum(map(mul, u, v))

def to_vec(a, b):
    return (b[0] - a[0], b[1] - a[1])

def norm(v):
    return math.hypot(*v)

def side_lengths(ax, ay, bx, by, cx, cy):
    pts = [(ax, ay), (bx, by), (cx, cy)]
    cyc = lambda arr: arr + [arr[0]]
    lens = tuple(norm(to_vec(*pair(*pts[i]), *pair(*pts[i+1]))) for i in range(3))
    return lens

def cosine_law(a, b, c):
    # cos(angle opposite to a)
    return truediv(add(square(b),square(c)) - square(a), mul(2,b,c))

def triangle_area(a, b, c):
    # Heron's formula, used in needlessly abstract way
    s = truediv(add(add(a,b),c),2)
    return math.sqrt(reduce(mul, (s - a, s - b, s - c, s)))

def angle_from_cos(cosv):
    return math.degrees(math.acos(cosv))

def inradius(area, a, b, c):
    return truediv(mul(2, area), add(add(a, b), c))

def tan_quarter_angle(angle):
    return round(math.tan(math.radians(truediv(angle, 4))), 10)

def malfatti_radii(a, b, c, A, B, C, r):
    tA, tB, tC = (tan_quarter_angle(angle) for angle in (A, B, C))
    f = lambda u, v, w: truediv(mul(add(1,v), add(1,w)), mul(2, add(1,u)))
    r1 = mul(f(tA, tB, tC), r)
    r2 = mul(f(tB, tC, tA), r)
    r3 = mul(f(tC, tA, tB), r)
    return r1, r2, r3

def main():
    while True:
        data = list(map(int, input().split()))
        if not any(data):
            break
        (x1, y1, x2, y2, x3, y3) = data
        # Overcomplicate distance computation
        vertices = [(x1, y1), (x2, y2), (x3, y3)]
        a, b, c = (dist(vertices[1], vertices[2]), dist(vertices[0], vertices[2]), dist(vertices[0], vertices[1]))
        
        # Overcomplicate cosine law
        cosA, cosB, cosC = map(lambda triple: round(cosine_law(*triple), 10),
                               [(a, b, c), (b, c, a), (c, a, b)])
        # Angles
        A, B, C = map(angle_from_cos, (cosA, cosB, cosC))
        
        # Area (law of sines, unnecessarily)
        S = truediv(mul(a, c, math.sin(math.radians(B))),2)
        r = truediv(mul(2,S), (a + b + c))
        
        r1, r2, r3 = malfatti_radii(a, b, c, A, B, C, r)
        print(r1, r2, r3)

if __name__ == "__main__":
    main()