from bisect import bisect_left
n = int(input())
a = list(map(int, input().split()))
a.append(1000000001)  # > 1,000,000,000
q = int(input())
for i in range(q):
	k = int(input())
	p = bisect_left(a, k)
	print(1 if a[p] == k else 0)