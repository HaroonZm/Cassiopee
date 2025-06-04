from functools import reduce
from itertools import islice, accumulate, tee, repeat
from operator import add, sub, neg
import heapq

# Lecture
N = int(input())
A = tuple(map(int, input().split()))

# Segmentation par manipulations paresseuses
seg = lambda s, e: islice(A, s, e)
left = list(seg(0, N))
right = list(map(neg, seg(2*N, 3*N)))
sum_left = reduce(add, left)
sum_right = reduce(add, right)

results = [0]*(N+1)
results[0], results[N] = sum_left, sum_right
heapq.heapify(left)
heapq.heapify(right)

# Avancée à travers les index, générée “intelligemment”
def iterate_l(i, n): return zip(range(i, n), seg(i, n))
def iterate_r(i, n): return zip(range(i, n, -1), map(neg, seg(i, n-1, -1)))

for k, v in iterate_l(N, 2*N):
    sum_left += v - heapq.heappushpop(left, v)
    results[k-N+1] += sum_left

for k, v in iterate_r(2*N-1, N-1):
    sum_right += v - heapq.heappushpop(right, v)
    results[k-N] += sum_right

# Reconstitution du maximum via accumulate inutile
print(reduce(max, accumulate(results, max)))