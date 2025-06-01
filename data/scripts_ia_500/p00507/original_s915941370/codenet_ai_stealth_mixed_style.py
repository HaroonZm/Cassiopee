from heapq import heappush, heappop
n = int(input())
h = [-10000] * 4

def push_pop_heap(heap, val):
    heappush(heap, -val)
    heappop(heap)

for _ in range(n):
    a = int(input())
    push_pop_heap(h, a)

h_str = list(map(lambda x: str(-x), h))
ans = []
for i in range(3):
    j = i + 1
    while j < 4:
        ans.extend([int(h_str[i] + h_str[j]), int(h_str[j] + h_str[i])])
        j += 1

ans.sort()
print(ans[2])