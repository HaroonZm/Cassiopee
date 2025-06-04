import sys
from datetime import date

eras = [
    ("meiji", date(1868, 9, 8), date(1912, 7, 29)),
    ("taisho", date(1912, 7, 30), date(1926, 12, 24)),
    ("showa", date(1926, 12, 25), date(1989, 1, 7)),
    ("heisei", date(1989, 1, 8), date(9999, 12, 31)),
]

for line in sys.stdin:
    line=line.strip()
    if not line:
        continue
    y,m,d = map(int, line.split())
    dt = date(y,m,d)
    for name, start, end in eras:
        if start <= dt <= end:
            era_year = y - start.year + 1
            print(name, era_year, m, d)
            break
    else:
        print("pre-meiji")