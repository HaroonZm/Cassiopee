# AOJ 1502: War
# Python3 2018.7.13 bal4u

n = int(input())
ans = 1
h = [0]*126
for i in range(n):
	v = int(input())
	if v <= 125: h[v] += 1
	ans += v
s = 0
for i in range(1, 126):
	s += h[i-1]
	if n > s+4*i: ans -= n-(s+4*i)
print(ans)