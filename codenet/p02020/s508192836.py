n = int(input())
a = list(map(int,input().split()))
if sum(a) % 2 == 0:
	print(sum(a) // 2)
else:
	a.sort()
	mi = 10000
	for i in a:
		if i % 2 == 1:
			mi = i
			break
	print((sum(a) - mi) // 2)