N = int(input())
holidays = []
for _ in range(N):
    M, D, V, S = map(int, input().split())
    start = (M - 1) * 30 + (D - 1)
    end = (start + V - 1) % 360
    holidays.append((start, end, V, S))

def dist(a, b):
    """Distance from day a to day b on circular calendar."""
    if b >= a:
        return b - a
    return b + 360 - a

min_crowd = float('inf')

for day in range(360):
    max_influence = 0
    for start, end, V, S in holidays:
        # Check if day is in the holiday period (considering circular array)
        if start <= end:
            inside = (start <= day <= end)
        else:
            inside = (day >= start or day <= end)
        if inside:
            influence = S
        else:
            dist_start = dist(day, start)
            dist_end = dist(end, day)
            d = min(dist_start, dist_end)
            influence = max(0, S - d)
        if influence > max_influence:
            max_influence = influence
    if max_influence < min_crowd:
        min_crowd = max_influence

print(min_crowd)