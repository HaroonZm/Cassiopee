import sys

# バッジテストの基準タイム（秒）
badge_times = [
    ('AAA', 35.50, 71.00),
    ('AA', 37.50, 77.00),
    ('A', 40.00, 83.00),
    ('B', 43.00, 89.00),
    ('C', 50.00, 105.00),
    ('D', 55.00, 116.00),
    ('E', 70.00, 148.00),
]

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    t1_str, t2_str = line.split()
    t1 = float(t1_str)
    t2 = float(t2_str)

    result = 'NA'
    for grade, limit_500, limit_1000 in badge_times:
        if t1 < limit_500 and t2 < limit_1000:
            result = grade
            break
    print(result)