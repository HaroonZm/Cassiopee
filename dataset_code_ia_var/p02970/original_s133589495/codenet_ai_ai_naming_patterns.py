num_items, cover_range = map(int, input().split(' '))

current_coverage = 2 * cover_range + 1
coverage_count = 1
while num_items > current_coverage:
    coverage_count += 1
    current_coverage += 2 * cover_range + 1

print(coverage_count)