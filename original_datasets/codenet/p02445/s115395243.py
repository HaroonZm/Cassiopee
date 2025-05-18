# AOJ ITP2_4_C: Swap
# Python3 2018.6.24 bal4u

n = int(input())
a = list(map(int, input().split()))
q = int(input())
for i in range(q):
	b, e, t = map(int, input().split())
	s = t+e-b
	if t > b:
		a = a[:b] + a[t:s] + a[e:t] + a[b:e] + a[s:]
	else:
		a = a[:t] + a[b:e] + a[s:b] + a[t:s] + a[e:]
print(*a)