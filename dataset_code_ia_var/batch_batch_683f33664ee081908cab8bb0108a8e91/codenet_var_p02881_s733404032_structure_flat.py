import sys
import math

n = int(sys.stdin.readline().strip())
start = int(math.sqrt(n))
found = False
for i in range(start+1, 0, -1):
    if (n / i).is_integer():
        print(i - 1 + (n // i) - 1)
        found = True
        break
if not found:
    print("wrong...")