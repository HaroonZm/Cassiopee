r = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

import sys

for line in sys.stdin:
    line = line.strip()
    total = 0
    values = []
    for char in line:
        values.append(r[char])
    for i in range(len(values)):
        if i + 1 < len(values) and values[i] < values[i + 1]:
            total -= values[i]
        else:
            total += values[i]
    print(total)