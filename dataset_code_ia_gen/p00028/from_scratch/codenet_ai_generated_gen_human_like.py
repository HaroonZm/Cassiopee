from collections import Counter
import sys

numbers = []
for line in sys.stdin:
    line = line.strip()
    if line.isdigit():
        numbers.append(int(line))

count = Counter(numbers)
max_freq = max(count.values())
modes = [num for num, freq in count.items() if freq == max_freq]
modes.sort()
for mode in modes:
    print(mode)