import heapq

N = int(input())
h = [4, 7]
heapq.heapify(h)

while True:
    n = heapq.heappop(h)

    if n > N:
        print('No')
        break

    if n == N:
        print('Yes')
        break

    heapq.heappush(h, n + 4)
    heapq.heappush(h, n + 7)