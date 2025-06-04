while True:
    line = input().strip()
    if line == '0 0':
        break
    n, w = map(int, line.split())
    values = [int(input()) for _ in range(n)]
    max_val = max(values)
    intervals_count = max_val // w + 1

    counts = [0] * intervals_count
    for v in values:
        idx = v // w
        counts[idx] += 1

    max_count = max(counts)
    if max_count == 0:
        # No bars, ink used just 0.01
        print(0.01)
        continue

    # Darkness levels from left (black=1) to right (white=0): linear decrease
    # For k intervals, darkness for i-th bar (0-based) = 1 - i/(k-1)
    # Amount of ink per bar = area * darkness
    # Here width w, height proportional to counts[i]/max_count
    # So area = w * (counts[i]/max_count)
    # Ink for bar i = w * (counts[i]/max_count) * darkness
    # Total ink = sum over bars + 0.01

    total_ink = 0.0
    denom = intervals_count - 1
    for i in range(intervals_count):
        height_ratio = counts[i] / max_count
        darkness = 1 - (i / denom) if denom > 0 else 1  # if only 1 interval, darkness=1
        bar_ink = w * height_ratio * darkness
        total_ink += bar_ink

    # One unit ink used for highest bar black means: highest bar ink should be 1 unit
    # But we already computed bar ink as proportional area*darkness and with given units
    # So the total ink computed corresponds to units. Just add 0.01 fixed ink

    total_ink += 0.01
    print(total_ink)