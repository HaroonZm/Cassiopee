import sys
import re

total = 0
for line in sys.stdin:
    nums = re.findall(r'\d+', line)
    total += sum(map(int, nums))
print(total)