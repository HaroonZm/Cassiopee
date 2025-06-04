from sys import stdin

g, l = 9.8, 4.9

def compute_n(v):
    t = v / g
    y = l * t ** 2
    return int(y / 5 + 2)

for line in stdin:
    try:
        v = float(line)
        print(compute_n(v))
    except ValueError:
        continue