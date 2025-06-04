range_start, range_center = map(int, input().split())
range_values = [value for value in range(range_center - range_start + 1, range_center + range_start)]
print(*range_values)