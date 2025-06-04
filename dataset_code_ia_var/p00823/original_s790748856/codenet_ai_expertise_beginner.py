import math
import string
import sys

sys.setrecursionlimit(10000000)
inf = 10 ** 20
eps = 1.0 / (10 ** 10)
mod = 10 ** 9 + 7

# Directions
dd = [(-1,0), (0,1), (1,0), (0,-1)]
ddn = [(-1,0), (-1,1), (0,1), (1,1), (1,0), (1,-1), (0,-1), (-1,-1)]

def LI():
    return [int(x) for x in sys.stdin.readline().split()]

def LI_():
    return [int(x)-1 for x in sys.stdin.readline().split()]

def LF():
    return [float(x) for x in sys.stdin.readline().split()]

def LS():
    return sys.stdin.readline().split()

def I():
    return int(sys.stdin.readline())

def F():
    return float(sys.stdin.readline())

def S():
    return input()

def pf(s):
    print(s, flush=True)

def _kosa(a1, a2, b1, b2):
    x1, y1, _ = a1
    x2, y2, _ = a2
    x3, y3, _ = b1
    x4, y4, _ = b2

    tc = (x1 - x2) * (y3 - y1) + (y1 - y2) * (x1 - x3)
    td = (x1 - x2) * (y4 - y1) + (y1 - y2) * (x1 - x4)
    return tc * td < 0

def kosa(a1, a2, b1, b2):
    return _kosa(a1, a2, b1, b2) and _kosa(b1, b2, a1, a2)

def distance(x1, y1, x2, y2):
    dx = x1 - x2
    dy = y1 - y2
    return math.sqrt(dx * dx + dy * dy)

def distance3(p1, p2, p3):
    x1, y1, _ = p1
    x2, y2, _ = p2
    x3, y3, _ = p3

    ax = x2 - x1
    ay = y2 - y1
    bx = x3 - x1
    by = y3 - y1

    if (ax * ax + ay * ay) == 0:
        return distance(x1, y1, x3, y3)
    r = (ax * bx + ay * by) / (ax * ax + ay * ay)
    if r <= 0:
        return distance(x1, y1, x3, y3)
    if r >= 1:
        return distance(x2, y2, x3, y3)
    return distance(x1 + r * ax, y1 + r * ay, x3, y3)

def main():
    rr = []

    d = {}

    # Read key-value pairs
    while True:
        s = S()
        if s == 'END_OF_FIRST_PART':
            break
        a, b = s.split()
        d[a] = int(b)

    def f(s):
        a = []
        for c in s:
            if "0" <= c <= "9":
                if len(a) > 0 and isinstance(a[-1], int):
                    a[-1] = a[-1] * 10 + int(c)
                else:
                    a.append(int(c))
            elif c in string.ascii_lowercase:
                if len(a) < 1 or isinstance(a[-1], int):
                    return 'UNKNOWN'
                if isinstance(a[-1], int):
                    a[-1] = str(a[-1]) + c
                else:
                    a.append(c)
            else:
                a.append(c)

        # Now, verify all variables are in d
        for c in a:
            if isinstance(c, int) or c == '(' or c == ')':
                continue
            if c not in d:
                return 'UNKNOWN'

        def _f(a):
            if '(' in a:
                # Evaluate parentheses
                i = a.index('(')
                level = 1
                for j in range(i+1, len(a)):
                    if a[j] == '(':
                        level += 1
                    elif a[j] == ')':
                        level -= 1
                        if level == 0:
                            t = _f(a[i+1:j])
                            if t is None:
                                return None
                            # Check if we have multiplier
                            if len(a) > j+1 and isinstance(a[j+1], int):
                                t = t * a[j+1]
                                return _f(a[:i] + [-t] + a[j+2:])
                            return _f(a[:i] + [-t] + a[j+1:])
                return None
            r = 0
            i = 0
            while i < len(a):
                c = a[i]
                if isinstance(c, int):
                    r += abs(c)
                    i += 1
                    continue
                if (i+1 < len(a)) and isinstance(a[i+1], int) and a[i+1] >= 0:
                    r += (d[c] - 1) * a[i+1]
                    i += 2
                else:
                    r += d[c]
                    i += 1
            return r

        return _f(a)

    # Now process queries
    while True:
        s = S()
        if s == '0':
            break
        rr.append(f(s))

    return '\n'.join([str(x) for x in rr])

print(main())