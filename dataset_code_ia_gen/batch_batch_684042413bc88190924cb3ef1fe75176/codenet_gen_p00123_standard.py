import sys

levels = [
    ('AAA', 35.50, 71.00),
    ('AA', 37.50, 77.00),
    ('A', 40.00, 83.00),
    ('B', 43.00, 89.00),
    ('C', 50.00, 105.00),
    ('D', 55.00, 116.00),
    ('E', 70.00, 148.00),
]

for line in sys.stdin:
    if not line.strip():
        continue
    t1, t2 = map(float, line.split())
    for lvl, t1_lim, t2_lim in levels:
        if t1 < t1_lim and t2 < t2_lim:
            print(lvl)
            break
    else:
        print('NA')