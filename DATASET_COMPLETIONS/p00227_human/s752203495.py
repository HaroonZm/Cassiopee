# try-except is necessary for avoiding Runtime Error 
while 1:
	try:
		n,m=map(int,raw_input().split())
		if n==0:break
		v=sorted(map(int,raw_input().split()))[::-1]
		for i in range(m-1,n,m):
			v[i]=0
		print sum(v)
	except:
		pass