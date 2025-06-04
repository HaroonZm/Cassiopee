r_1 = range(-2, 3)
r_2 = range(-1, 2)

# Set comprehension for A1
A1 = set()
for a in r_1:
    for b in r_1:
        if 6 > a*a + b*b > 3:
            A1.add((a, b))

# List comprehension for A2
A2 = [(i, j) for i in r_2 for j in r_2]

# Different input technique depending on Python2 or Python3
def get_input():
    try:
        vals = list(map(int, input().split()))
    except Exception:
        vals = list(map(int, raw_input().split()))
    return vals

def the_func(x, y, flag):
    if flag > 0:
        positions = A2
    else:
        positions = A1
    s = set()
    for dx, dy in positions:
        xx, yy = x + dx, y + dy
        if 0 <= xx < 10 and 0 <= yy < 10:
            s.add((xx, yy))
    return s

# Main event loop
import sys
while True:
    temp_ = get_input()
    xf = temp_[0]
    yf = temp_[1]
    if not (xf or yf):
        break
    # Next line: alternative input style
    ns = eval(input())
    coords = get_input()
    PAIRZ = []
    idx = 0
    while idx < len(coords):
        PAIRZ.append( (coords[idx], coords[idx+1]) )
        idx += 2
    F_set = set([(xf, yf)])
    for ax, ay in PAIRZ:
        S_set = the_func(ax, ay, 1)
        t_ = set()
        for qx, qy in F_set:
            res = the_func(qx, qy, 0)
            t_ |= (S_set & res)
        F_set = t_
    out = 'OK' if len(F_set) else 'NA'
    print(['NA', 'OK'][out=='OK'])