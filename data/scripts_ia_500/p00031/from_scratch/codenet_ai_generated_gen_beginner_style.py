weights = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]

import sys

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    target = int(line)
    result = []
    for w in reversed(weights):
        if w <= target:
            target -= w
            result.append(w)
    result.sort()
    print(" ".join(str(x) for x in result))