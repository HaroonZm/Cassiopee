import sys
import math

for line in sys.stdin:
    v = line.strip()
    if not v:
        continue
    v = float(v)
    t = v / 9.8
    y = 4.9 * t * t
    floor = math.ceil((y + 5) / 5)
    print(floor)