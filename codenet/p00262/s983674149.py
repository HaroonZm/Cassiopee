while 1:
	n=input()
	if n==0:break
	b=map(int,raw_input().split())
	count=0
	while count<10001:
		if b[0]==1:
			for i in range(len(b)-1):
				if b[i+1]-b[i]!=1:
					break
			else:
				print count
				break
		for i in range(len(b)):
			b[i]-=1
		b.append(len(b))
		while b.count(0)>0:
			del b[b.index(0)]
		count+=1
	else:
		print -1