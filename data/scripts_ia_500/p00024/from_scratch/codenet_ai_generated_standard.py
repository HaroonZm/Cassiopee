import sys
import math

for line in sys.stdin:
    v = float(line.strip())
    t = v / 9.8
    y = 4.9 * t * t
    floor = math.ceil((y + 5) / 5)
    print(floor)