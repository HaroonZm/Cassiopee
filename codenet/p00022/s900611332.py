while 1:
	n=int(input())
	if n==0: break
	a=[int(input()) for i in range(n)]
	temp = 0
	most = -999999999
	for i in range(n):
		temp = 0
		for j in range(i,n):
			temp +=	a[j]
			if temp > most:
				most = temp
	print(most)