from heapq import heapify, heappop, heappush

N, M, K = (int(x) for x in input().split())
A, B, C = [int(val) for val in input().split()]
T = int(input())
S = list(map(lambda x: int(x)-1, (input() for _ in range(M))))

def f(rt, rn):
    result = rt // A
    if result > rn - 1:
        return rn - 1
    return result

answer = 0
queue = []

i = 0
while i < M - 1:
    start = S[i]
    end = S[i+1]
    if B * start <= T:
        remaining_time = T - B * start
        remaining_nodes = end - start
        
        k = f(remaining_time, remaining_nodes)
        answer += k + 1
        
        remaining_time -= (k + 1) * C
        remaining_nodes -= (k + 1)
        
        k0 = f(remaining_time, remaining_nodes)
        if k0 >= 0:
            queue.append((-k0, remaining_time, remaining_nodes))
    i += 1

if B * S[-1] <= T:
    answer += 1

heapify(queue)

for _ in range(K - M):
    if len(queue) == 0:
        break
    k, rt, rn = heappop(queue)
    k = -k
    rt -= (k + 1) * C
    rn -= (k + 1)
    
    answer += k + 1
    
    k0 = f(rt, rn)
    if k0 >= 0:
        heappush(queue, (-k0, rt, rn))

print(answer - 1)