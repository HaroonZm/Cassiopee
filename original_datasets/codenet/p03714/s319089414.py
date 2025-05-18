#########################ABC解説実装#########################
import heapq
N=int(input())
A=list(map(int, input().split()))

left, right = A[:N], [-1 * i for i in A[2*N:]]
sum_left, sum_right = sum(left), sum(right)

results = [0] * (N+1)
results[0] = sum_left
results[N] = sum_right

heapq.heapify(left)
heapq.heapify(right)

for i in range(N, 2*N):
    v = A[i]
    p = heapq.heappushpop(left, v)
    sum_left += v - p
    results[i-N+1] += sum_left
    
for i in range(2*N-1, N-1, -1):
    v = -1 * A[i]
    p = heapq.heappushpop(right, v)
    sum_right += v - p
    results[i-N] += sum_right
print(max(results))