import sys

lines = sys.stdin.read().strip('\n').split('\n')

if '' in lines:
    empty_index = lines.index('')
    last_month_lines = lines[:empty_index]
    this_month_lines = lines[empty_index+1:]
else:
    last_month_lines = []
    this_month_lines = lines

last_month_counts = {}
this_month_counts = {}

for line in last_month_lines:
    if line.strip() == '':
        continue
    parts = line.strip().split(',')
    if len(parts) != 2:
        continue
    c = int(parts[0])
    # d = int(parts[1])  # 取引日は使わない
    if c in last_month_counts:
        last_month_counts[c] += 1
    else:
        last_month_counts[c] = 1

for line in this_month_lines:
    if line.strip() == '':
        continue
    parts = line.strip().split(',')
    if len(parts) != 2:
        continue
    c = int(parts[0])
    # d = int(parts[1])  # 取引日は使わない
    if c in this_month_counts:
        this_month_counts[c] += 1
    else:
        this_month_counts[c] = 1

result = []

for c in this_month_counts:
    if c in last_month_counts:
        total = this_month_counts[c] + last_month_counts[c]
        result.append((c, total))

result.sort(key=lambda x: x[0])

for c, total in result:
    print(c, total)