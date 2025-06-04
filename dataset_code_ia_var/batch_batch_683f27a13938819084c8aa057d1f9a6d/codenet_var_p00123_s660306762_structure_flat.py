import sys

criteria = [
    (35.50, 71.0, 'AAA'),
    (37.50, 77.0, 'AA'),
    (40.0, 83.0, 'A'),
    (43.0, 89.0, 'B'),
    (50.0, 105.0, 'C'),
    (55.0, 116.0, 'D'),
    (70.0, 148.0, 'E')
]

for line in sys.stdin:
    r500, r1000 = [float(x) for x in line.strip().split()]
    rank = None
    for c500, c1000, r in criteria:
        if r500 < c500 and r1000 < c1000:
            rank = r
            break
    if rank is None:
        rank = 'NA'
    print(rank)