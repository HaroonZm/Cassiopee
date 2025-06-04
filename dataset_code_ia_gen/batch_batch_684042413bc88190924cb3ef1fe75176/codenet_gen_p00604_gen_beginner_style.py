import sys

for line in sys.stdin:
    line = line.strip()
    if line == '':
        continue
    N = int(line)
    if N == 0:
        print(0)
        continue
    times_line = sys.stdin.readline().strip()
    times = list(map(int, times_line.split()))
    times.sort()
    total = 0
    current = 0
    for t in times:
        current += t
        total += current
    print(total)