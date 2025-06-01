import sys

for line in sys.stdin:
    print(*sorted(map(int, line.split()), reverse=True))