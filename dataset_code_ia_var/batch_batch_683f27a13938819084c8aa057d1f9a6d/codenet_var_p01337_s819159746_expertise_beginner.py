import math

def make_func1(a, b, c, d):
    def f(X):
        return a*X*X*X + b*X*X + c*X + d
    return f

def make_func2(a, b, c):
    def f(x):
        return 3*a*x*x + 2*b*x + c
    return f

i = int(input())
for j in range(i):
    a, b, c, d = map(int, input().split())
    fX = make_func1(a, b, c, d)
    fx = make_func2(a, b, c)
    D_4 = b*b - 3*a*c

    pos = 0
    neg = 0

    if D_4 <= 0:
        if a > 0:
            if d < 0:
                pos = 1
                neg = 0
            if d == 0:
                pos = 0
                neg = 0
            if d > 0:
                pos = 0
                neg = 1
        if a < 0:
            if d < 0:
                pos = 0
                neg = 1
            if d == 0:
                pos = 0
                neg = 0
            if d > 0:
                pos = 1
                neg = 0

    if D_4 > 0:
        if a > 0:
            p = (-b - math.sqrt(b*b - 3*a*c)) / (3*a)
            q = (-b + math.sqrt(b*b - 3*a*c)) / (3*a)
            if fX(q) > 0 or fX(p) < 0:
                if d < 0:
                    pos = 1
                    neg = 0
                if d == 0:
                    pos = 0
                    neg = 0
                if d > 0:
                    pos = 0
                    neg = 1
            if fX(q) == 0:
                if d < 0:
                    pos = 3
                    neg = 0
                if d == 0 and p > 0:
                    pos = 2
                    neg = 0
                if d > 0 and q > 0:
                    pos = 2
                    neg = 1
                if d == 0 and q == 0:
                    pos = 0
                    neg = 1
                if d > 0 and q < 0:
                    pos = 0
                    neg = 3
            if fX(p) == 0:
                if d < 0 and p > 0:
                    pos = 3
                    neg = 0
                if d == 0 and p == 0:
                    pos = 1
                    neg = 0
                if d < 0 and p < 0:
                    pos = 1
                    neg = 2
                if d == 0 and q < 0:
                    pos = 0
                    neg = 2
                if d > 0 and q < 0:
                    pos = 0
                    neg = 3
            if fX(q) < 0 and fX(p) > 0:
                if d < 0 and p > 0:
                    pos = 3
                    neg = 0
                if d == 0 and p > 0:
                    pos = 2
                    neg = 0
                if d > 0 and q > 0:
                    pos = 2
                    neg = 1
                if d == 0 and (p < 0 and q > 0):
                    pos = 1
                    neg = 1
                if d < 0 and p < 0:
                    pos = 1
                    neg = 2
                if d == 0 and q < 0:
                    pos = 0
                    neg = 2
                if d > 0 and q < 0:
                    pos = 0
                    neg = 3
        if a < 0:
            p = (-b + math.sqrt(b*b - 3*a*c)) / (3*a)
            q = (-b - math.sqrt(b*b - 3*a*c)) / (3*a)
            if fX(p) > 0 or fX(q) < 0:
                if d < 0:
                    pos = 0
                    neg = 1
                if d == 0:
                    pos = 0
                    neg = 0
                if d > 0:
                    pos = 1
                    neg = 0
            if fX(p) == 0:
                if d > 0 and p > 0:
                    pos = 3
                    neg = 0
                if d == 0 and p == 0:
                    pos = 1
                    neg = 0
                if d > 0 and p < 0:
                    pos = 1
                    neg = 2
                if d == 0 and q < 0:
                    pos = 0
                    neg = 2
                if d < 0 and q < 0:
                    pos = 0
                    neg = 3
            if fX(q) == 0:
                if d > 0 and p > 0:
                    pos = 3
                    neg = 0
                if d == 0 and p > 0:
                    pos = 2
                    neg = 0
                if d < 0 and q > 0:
                    pos = 2
                    neg = 1
                if d == 0 and q == 0:
                    pos = 0
                    neg = 1
                if d < 0 and q < 0:
                    pos = 0
                    neg = 3
            if fX(p) < 0 and fX(q) > 0:
                if d > 0 and p > 0:
                    pos = 3
                    neg = 0
                if d == 0 and p > 0:
                    pos = 2
                    neg = 0
                if d < 0 and q > 0:
                    pos = 2
                    neg = 1
                if d == 0 and (p < 0 and q > 0):
                    pos = 1
                    neg = 1
                if d > 0 and p < 0:
                    pos = 1
                    neg = 2
                if d == 0 and q < 0:
                    pos = 0
                    neg = 2
                if d < 0 and q < 0:
                    pos = 0
                    neg = 3

    print(pos, neg)