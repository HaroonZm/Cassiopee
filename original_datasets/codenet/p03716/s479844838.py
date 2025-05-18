import heapq

N = int(input())
src = list(map(int,input().split()))

s1 = sum(src[:N])
r1 = [s1]
q1 = src[:N]
heapq.heapify(q1)
for i in range(N):
    heapq.heappush(q1,src[N+i])
    p = heapq.heappop(q1)
    r1.append(r1[-1] + src[N+i] - p)

s2 = -sum(src[-N:])
r2 = [s2]
q2 = [-a for a in src[-N:]]
heapq.heapify(q2)
for i in range(N):
    heapq.heappush(q2,-src[-N-i-1])
    p = heapq.heappop(q2)
    r2.append(r2[-1] - src[-N-i-1] - p)

ans = -float('inf')
for a,b in zip(r1,r2[::-1]):
    ans = max(ans, a+b)
print(ans)