def make_line(line_str):
    parts = line_str.split()
    return complex(int(parts[0]), int(parts[1])), complex(int(parts[2]), int(parts[3]))

def cross_point(l1, l2):
    def cross(a, b):
        return a.real * b.imag - a.imag * b.real

    p = [l1[0], l1[1], l2[0], l2[1]]
    vA = p[1] - p[0]
    vB = p[3] - p[2]
    a1 = cross(vB, p[0] - p[2])
    a2 = cross(vB, p[1] - p[2])
    denom = a1 + a2
    if denom == 0:
        return None
    t = a1 / denom
    if t > 0 and t < 1:
        pt = (p[0] + vA * t) * 1e10
        x, y = int(pt.real), int(pt.imag)
        return tuple([x, y])
    return None

from functools import reduce

def main():
    while True:
        try:
            n = int(input())
        except:
            break
        if n == 0:
            break
        d = []
        c = 0
        for _ in range(n):
            d.append(make_line(input()))
        j = 0
        while j < n:
            this_line = d[j]
            prev = d[:j]
            found = set(map(lambda l: cross_point(this_line, l), prev))
            if None in found:
                found.remove(None)
            c += len(found)
            j += 1
        print(1 + n + c)
main()