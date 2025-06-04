range_count = int(input())
total_count = 0
for range_index in range(range_count):
    range_start, range_end = map(int, input().split())
    total_count += range_end - range_start + 1
print(total_count)