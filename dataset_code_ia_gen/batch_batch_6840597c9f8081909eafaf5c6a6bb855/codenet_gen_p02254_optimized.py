from collections import Counter
from heapq import heapify, heappop, heappush

S = input()
freq = Counter(S)
if len(freq) == 1:
    print(len(S))
    exit()

heap = list(freq.values())
heapify(heap)

while len(heap) > 1:
    x = heappop(heap)
    y = heappop(heap)
    heappush(heap, x + y)

# Build code length mapping via simulation
# But we only have total sum in heap[0], so we must compute total cost during merges.

# To compute total cost (sum of freq * code length), we implement Huffman cost calculation below:

freqs = list(freq.values())
if len(freqs) == 1:
    print(len(S))
    exit()

heap = [(w, 0) for w in freqs]  # (weight, current_cost)
heapify(heap)
total_length = 0
while len(heap) > 1:
    (w1, c1) = heappop(heap)
    (w2, c2) = heappop(heap)
    merged_w = w1 + w2
    merged_c = max(c1, c2) + 1
    heappush(heap, (merged_w, merged_c))
    
# The root node:
root_w, root_c = heap[0]
# total bits = sum freq * depth
# We will get depth per character implicitly by this calculation:
# Actually no, above logic doesn't sum freq*depth, fix approach

# Correct approach:
# Use a priority queue of (weight, cost_sum):
# For leaves cost_sum=0
# For internal nodes cost_sum = cost_sum_x + cost_sum_y + x.weight + y.weight (sum of weight because each leaf's depth increased by 1)
# So:
heap = [(f, 0) for f in freqs]
heapify(heap)
while len(heap) > 1:
    (w1, c1) = heappop(heap)
    (w2, c2) = heappop(heap)
    merged_w = w1 + w2
    merged_c = c1 + c2 + merged_w
    heappush(heap, (merged_w, merged_c))
print(heap[0][1])