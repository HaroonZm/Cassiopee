import sys

def calcul(v):
    g = 9.8
    l = 4.9
    t = v / g
    y = l * (t ** 2)
    return y / 5 + 2

for line in sys.stdin:
    try:
        v = float(line.strip())
        n = calcul(v)
        print round(n)
    except ValueError:
        continue