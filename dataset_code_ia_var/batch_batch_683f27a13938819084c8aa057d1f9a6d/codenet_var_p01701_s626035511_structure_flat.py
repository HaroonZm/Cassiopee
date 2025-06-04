from fractions import Fraction

while True:
    s = input()
    if s == "#":
        break

    idx = 0
    n = None
    d = 0

    while True:
        if s[idx] == 'n':
            if idx + 5 < len(s):
                if n is None:
                    n = 0
                n = (n - 45) * 2
                d += 1
                idx += 5
            else:
                if n is None:
                    n = 0
                break
        else:
            if idx + 4 < len(s):
                if n is None:
                    n = 90
                n = (n + 45) * 2
                d += 1
                idx += 4
            else:
                if n is None:
                    n = 90
                break

    d = 2 ** d
    ans = Fraction(n, d)
    print(ans)