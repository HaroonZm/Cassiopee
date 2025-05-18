import heapq

pq = []
# 

W, H = map(int, input().split())
for i in range(W):
	heapq.heappush(pq, (int(input()), 'W'))
for i in range(H):
	heapq.heappush(pq, (int(input()), 'H'))

W += 1
H += 1

ans = 0
while pq:
	(num, dire) = heapq.heappop(pq)
	if dire == 'W':
		ans += num * H
		W -= 1
	else:
		ans += num * W
		H -= 1

print(ans)