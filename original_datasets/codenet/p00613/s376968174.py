while True:
	K = eval(input())
	if K == 0:
		break
	total = sum([eval(c) for c in input().split()])
	print(int(total/(K-1)))