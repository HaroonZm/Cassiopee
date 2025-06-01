from collections import deque

BIG_NUM = 2_000_000_000

num_lane, num_info = map(int, input().split())
lanes = [deque() for _ in range(num_lane)]

for _ in range(num_info):
    cmd, val = map(int, input().split())
    if cmd == 0:
        print(lanes[val - 1].popleft())
    else:
        min_lane = min(range(num_lane), key=lambda i: len(lanes[i]))
        lanes[min_lane].append(val)