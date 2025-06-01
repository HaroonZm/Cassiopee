import sys

def minimal_penalty(times):
    times.sort()
    total = 0
    elapsed = 0
    for t in times:
        elapsed += t
        total += elapsed
    return total

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    n = int(line)
    if n == 0:
        print(0)
        continue
    times = list(map(int, sys.stdin.readline().split()))
    print(minimal_penalty(times))