import sys
import re

total = 0
for line in sys.stdin:
    total += sum(map(int, re.findall(r'\d+', line)))
print(total)