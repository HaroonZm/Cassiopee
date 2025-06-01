from collections import Counter
import sys

nums = [int(line) for line in sys.stdin if line.strip()]
counts = Counter(nums)
max_freq = max(counts.values())
modes = sorted([num for num, freq in counts.items() if freq == max_freq])
for mode in modes:
    print(mode)