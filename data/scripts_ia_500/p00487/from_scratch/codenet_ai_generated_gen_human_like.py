import sys
import heapq

input = sys.stdin.readline

N = int(input())
microbes = [tuple(map(int, input().split())) for _ in range(N)]

# Sort microbes by their capacity b_i in ascending order
microbes.sort(key=lambda x: x[1])

# Use a max heap to keep track of selected microbes' foo release amounts a_i
heap = []
sum_a = 0
max_count = 0

for a, b in microbes:
    # Add current microbe's foo release to heap and sum
    heapq.heappush(heap, -a)
    sum_a += a

    # If average foo intake exceeds current microbe's capacity, remove the largest a_i
    while sum_a > b * len(heap):
        removed = -heapq.heappop(heap)
        sum_a -= removed

    # Update max count
    max_count = max(max_count, len(heap))

print(max_count)