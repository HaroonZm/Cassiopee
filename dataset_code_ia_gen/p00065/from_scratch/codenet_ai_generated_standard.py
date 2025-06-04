from sys import stdin

# Read input until empty line
lines = [line.strip() for line in stdin if line.strip() != '']
half = len(lines) // 2
last_month = lines[:half]
this_month = lines[half:]

def parse_data(data):
    counts = {}
    for line in data:
        c, d = line.split(',')
        c = int(c)
        counts[c] = counts.get(c, 0) + 1
    return counts

last_counts = parse_data(last_month)
this_counts = parse_data(this_month)

# 顧客番号が先月と今月の両方にあるものを抽出
common_customers = set(last_counts) & set(this_counts)

for c in sorted(common_customers):
    print(c, last_counts[c] + this_counts[c])