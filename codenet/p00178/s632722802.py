while 1:
	n=input()
	if n==0:break
	hmax=7500
	block=[map(int,raw_input().split()) for i in range(n)]
	field=[[0]*5 for i in range(hmax)]
	h=0
	for d,p,q in block:
		if d==1:
			for li in range(h,-2,-1):
				if field[li][q-1:q+p-1]!=[0]*p or li==-1:
					field[li+1][q-1:q+p-1]=[1]*p
					h=max(h,li+2)
					break
		else:
			for li in range(h,-2,-1):
				if field[li][q-1]!=0 or li==-1:
					for i in range(p):
						field[li+i+1][q-1]=1
					h=max(h,li+1+p)
					break
		i=0
		while 1:
			if field[i]==[1]*5:
				del field[i]
				h-=1
			elif field[i]==[0]*5:
				break
			else:
				i+=1
	print sum([sum(field[li]) for li in range(h)])