max_carbons = [0,1,2,4]
for n in range(4,31):
    max_carbons.append(max_carbons[n-1] + max_carbons[n-2] + max_carbons[n-3] +1)
import sys
for line in sys.stdin:
    n=line.strip()
    if not n: continue
    n=int(n)
    print(max_carbons[n])