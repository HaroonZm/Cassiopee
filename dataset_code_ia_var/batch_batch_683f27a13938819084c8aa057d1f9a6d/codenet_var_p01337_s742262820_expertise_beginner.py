n = int(input())

def f(a, b, c, d):
    def func(x):
        return a * x ** 3 + b * x ** 2 + c * x + d
    return func

for i in range(n):
    a, b, c, d = map(int, input().split())
    fx = f(a, b, c, d)
    D = b * b - 3 * a * c
    pl = 0
    mi = 0

    if D <= 0:
        if d == 0:
            pl = 0
            mi = 0
        elif (a > 0 and d < 0) or (a < 0 and d > 0):
            pl = 1
            mi = 0
        elif (a < 0 and d < 0) or (a > 0 and d > 0):
            pl = 0
            mi = 1
    else:
        if a > 0:
            al = (-b - D ** 0.5) / (3 * a)
            be = (-b + D ** 0.5) / (3 * a)
            if (fx(al) < 0 or fx(be) > 0) and d == 0:
                pl = 0
                mi = 0
            elif ((fx(al) < 0 or fx(be) > 0) and d > 0) or (fx(be) == 0 and d == 0 and be == 0):
                pl = 0
                mi = 1
            elif (fx(al) == 0 or (fx(al) > 0 and fx(be) < 0)) and d == 0 and be < 0:
                pl = 0
                mi = 2
            elif (fx(al) == 0 or fx(be) == 0 or (fx(al) > 0 and fx(be) < 0)) and d > 0 and be < 0:
                pl = 0
                mi = 3
            elif ((fx(al) < 0 or fx(be) > 0) and d < 0) or (fx(al) == 0 and d == 0 and al == 0):
                pl = 1
                mi = 0
            elif fx(al) > 0 and fx(be) < 0 and d == 0 and al < 0 and be > 0:
                pl = 1
                mi = 1
            elif (fx(al) == 0 or (fx(al) > 0 and fx(be) < 0)) and d < 0 and al < 0:
                pl = 1
                mi = 2
            elif (fx(be) == 0 or (fx(al) > 0 and fx(be) < 0)) and d == 0 and al > 0:
                pl = 2
                mi = 0
            elif (fx(be) == 0 or (fx(al) > 0 and fx(be) < 0)) and d > 0 and be > 0:
                pl = 2
                mi = 1
            elif ((fx(al) == 0 and al > 0) or fx(be) == 0 or (fx(al) > 0 and fx(be) < 0 and al > 0)) and d < 0:
                pl = 3
                mi = 0
        else:
            al = (-b + D ** 0.5) / (3 * a)
            be = (-b - D ** 0.5) / (3 * a)
            if (fx(al) > 0 or fx(be) < 0) and d == 0:
                pl = 0
                mi = 0
            elif ((fx(al) > 0 or fx(be) < 0) and d < 0) or (fx(be) == 0 and d == 0 and be == 0):
                pl = 0
                mi = 1
            elif (fx(al) == 0 or (fx(al) < 0 and fx(be) > 0)) and d == 0 and be < 0:
                pl = 0
                mi = 2
            elif (fx(al) == 0 or fx(be) == 0 or (fx(al) < 0 and fx(be) > 0)) and d < 0 and be < 0:
                pl = 0
                mi = 3
            elif ((fx(al) > 0 or fx(be) < 0) and d > 0) or (fx(al) == 0 and d == 0 and al == 0):
                pl = 1
                mi = 0
            elif fx(al) < 0 and fx(be) > 0 and d == 0 and al < 0 and be > 0:
                pl = 1
                mi = 1
            elif (fx(al) == 0 or (fx(al) < 0 and fx(be) > 0)) and d > 0 and al < 0:
                pl = 1
                mi = 2
            elif (fx(be) == 0 or (fx(al) < 0 and fx(be) > 0)) and d == 0 and al > 0:
                pl = 2
                mi = 0
            elif (fx(be) == 0 or (fx(al) < 0 and fx(be) > 0)) and d < 0 and be > 0:
                pl = 2
                mi = 1
            elif (fx(al) == 0 or fx(be) == 0 or (fx(al) < 0 and fx(be) > 0)) and d > 0 and al > 0:
                pl = 3
                mi = 0
    print(pl, mi)