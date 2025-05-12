# AOJ 1574: Gossip
# Python3 2018.7.13 bal4u

n, m = map(int, input().split())
a = list(map(int, input().split()))
pre = a[0]; d = 0
for x in a[1:]:
	d = max(d, x-pre)
	pre = x
print(max(n-pre, max(d>>1, a[0]-1)))