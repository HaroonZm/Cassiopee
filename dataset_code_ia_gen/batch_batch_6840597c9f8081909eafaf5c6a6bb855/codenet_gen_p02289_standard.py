import sys
import heapq

heap = []
for line in sys.stdin:
    line = line.strip()
    if line == 'end':
        break
    if line.startswith('insert'):
        _, k = line.split()
        heapq.heappush(heap, -int(k))
    elif line == 'extract':
        print(-heapq.heappop(heap))