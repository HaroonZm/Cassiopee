import sys

from functools import reduce

times = [int(sys.stdin.readline()) for _ in range(4)]
total_seconds = sum(times)
minutes, seconds = divmod(total_seconds, 60)
print(f"{minutes}\n{seconds}")