from collections import Counter
import sys

nums = [int(line) for line in sys.stdin if line.strip()]
counts = Counter(nums)
max_freq = max(counts.values())
modes = sorted(k for k, v in counts.items() if v == max_freq)
print('\n'.join(map(str, modes)))