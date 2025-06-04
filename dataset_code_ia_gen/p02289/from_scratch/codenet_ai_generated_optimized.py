import sys
import heapq

input = sys.stdin.readline
heap = []

while True:
    line = input()
    if not line:
        break
    cmd = line.split()
    if cmd[0] == 'insert':
        heapq.heappush(heap, -int(cmd[1]))
    elif cmd[0] == 'extract':
        print(-heapq.heappop(heap))
    elif cmd[0] == 'end':
        break