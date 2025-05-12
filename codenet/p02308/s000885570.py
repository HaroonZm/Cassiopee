from math import sqrt
from typing import List, Tuple

def project(point: complex, begin: complex, end: complex) -> complex:
    tmp = (point - begin) / (end - begin)
    return tmp.real * (end - begin) + begin

if __name__ == "__main__":
    x, y, r = map(int, input().split())
    c = complex(x, y)
    ans: List[Tuple[float, float, float, float]] = []
    q = int(input())

    for _ in range(q):
        res = []
        x, y, z, w = map(int, input().split())
        p1, p2 = complex(x, y), complex(z, w)
        proj = project(c, p1, p2)
        for i in (-1, 1):
            res.append(proj + i * sqrt(
                       r**2 - abs(c - proj)**2) * (p2 - p1) / abs(p2 - p1))
        res.sort(key=lambda x: (x.real, x.imag))
        ans.append((res[0].real, res[0].imag, res[1].real, res[1].imag))

    for a in ans:
        print("{:.6f} {:.6f} {:.6f} {:.6f}".format(*a))