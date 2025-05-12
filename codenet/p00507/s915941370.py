from heapq import heappush, heappop
n = input()
h = [-10000]*4
for i in range(n):
    a = input()
    heappush(h, -a)
    heappop(h)
h = [str(-a) for a in h]
ans = []
for i in range(3):
    for j in range(i+1, 4):
        ans.append(int(h[i]+h[j]))
        ans.append(int(h[j]+h[i]))
ans.sort()
print ans[2]