import heapq

pq = []

W_H = input().split()
W = int(W_H[0])
H = int(W_H[1])

i = 0
while i < W:
    n = int(input())
    heapq.heappush(pq, (n, 'W'))
    i += 1

i = 0
while i < H:
    n = int(input())
    heapq.heappush(pq, (n, 'H'))
    i += 1

W = W + 1
H = H + 1

ans = 0
while len(pq) != 0:
    item = heapq.heappop(pq)
    num = item[0]
    dire = item[1]
    if dire == 'W':
        ans = ans + num * H
        W = W - 1
    else:
        ans = ans + num * W
        H = H - 1

print(ans)