while True:
    line = input().strip()
    if line == '0 0':
        break
    parts = line.split()
    n = int(parts[0])
    w = int(parts[1])
    values = []
    for _ in range(n):
        v = int(input())
        values.append(v)
    max_value = max(values)
    intervals_count = max_value // w + 1
    counts = [0]*intervals_count
    for v in values:
        idx = v // w
        counts[idx] += 1
    max_count = max(counts)
    ink = 0.01
    for i in range(intervals_count):
        darkness = 1 - i/(intervals_count -1)
        height = counts[i]/max_count
        area = height * w
        ink += area * darkness
    print(ink)