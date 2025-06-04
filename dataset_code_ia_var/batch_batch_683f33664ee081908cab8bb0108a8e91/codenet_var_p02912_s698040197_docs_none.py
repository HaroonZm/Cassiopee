import heapq

N, M = map(int, input().split())
A = list(map(lambda x: int(x)*(-1), input().split()))
heapq.heapify(A)
for _ in range(M):
    num = heapq.heappop(A)
    heapq.heappush(A, (-num)//2*(-1))
print(sum(A)*(-1))