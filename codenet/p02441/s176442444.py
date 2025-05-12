# AOJ ITP2_3_C: Count
# Python3 2018.6.24 bal4u

n = int(input())
a = list(map(int, input().split()))
q = int(input())
for i in range(q):
	b, e, k = map(int, input().split())
	s = a[b:e]
	print(s.count(k))