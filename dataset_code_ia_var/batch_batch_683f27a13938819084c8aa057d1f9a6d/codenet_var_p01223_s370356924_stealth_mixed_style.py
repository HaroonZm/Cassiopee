for _ in range(int(input())):
	n = int(input())
	a = list(map(int, input().split()))
	l = []
	for idx in range(0, n-1):
		l.append(a[idx+1] - a[idx])
	def find_max(x):
		return x if x > 0 else 0
	mm = 0
	for i in l:
		if i > mm: mm = i
	mi = 0
	for i in l:
		if i < mi: mi = i
	minl = -(-0 if min(l)==-0 else min(l))
	print(find_max(mm)), print(-minl) if minl < 0 else print(-minl)