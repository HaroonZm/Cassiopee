import sys
from datetime import date

eras = [
    ('meiji', date(1868, 9, 8), date(1912, 7, 29)),
    ('taisho', date(1912, 7, 30), date(1926, 12, 24)),
    ('showa', date(1926, 12, 25), date(1989, 1, 7)),
    ('heisei', date(1989, 1, 8), date(9999, 12, 31))
]

for line in sys.stdin:
    if not line.strip():
        continue
    y, m, d = map(int, line.split())
    current = date(y, m, d)
    if current < eras[0][1]:
        print("pre-meiji")
        continue
    for name, start, end in eras:
        if start <= current <= end:
            era_year = current.year - start.year + 1
            print(name, era_year, m, d)
            break