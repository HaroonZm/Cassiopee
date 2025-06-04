def merge_intervals(intervals):
    intervals.sort()
    merged = []
    for start, end in intervals:
        if not merged or merged[-1][1] < start:
            merged.append([start, end])
        else:
            merged[-1][1] = max(merged[-1][1], end)
    return merged

def calculate_coverage_area(antennas):
    if not antennas:
        return 0.0
    xs = set()
    for x, y, r in antennas:
        xs.add(x - r)
        xs.add(x + r)
    xs = sorted(xs)

    area = 0.0
    for i in range(len(xs) - 1):
        x_left = xs[i]
        x_right = xs[i + 1]
        if x_right == x_left:
            continue
        segments = []
        for x, y, r in antennas:
            if x - r <= x_left < x + r:
                segments.append([y - r, y + r])
        merged = merge_intervals(segments)
        coverage_y = 0.0
        for start, end in merged:
            coverage_y += end - start
        area += coverage_y * (x_right - x_left)
    return area

def main():
    import sys
    dataset_id = 1
    lines = sys.stdin.read().strip().split('\n')
    idx = 0
    while True:
        if idx >= len(lines):
            break
        n = int(lines[idx])
        idx += 1
        if n == 0:
            break
        antennas = []
        for _ in range(n):
            x, y, r = map(float, lines[idx].split())
            idx += 1
            antennas.append((x, y, r))
        area = calculate_coverage_area(antennas)
        print(f"{dataset_id} {area:.2f}")
        dataset_id += 1

if __name__ == "__main__":
    main()