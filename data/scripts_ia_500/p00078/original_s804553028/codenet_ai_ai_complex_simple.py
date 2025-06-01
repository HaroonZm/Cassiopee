def print_board(A,n):
	from functools import reduce
	spaces=lambda x:reduce(lambda a,b:a+b,["   " if len(str(x))==1 else "  " if len(str(x))==2 else " " for _ in range(1)],"")
	for i in range(n):
		print(''.join((lambda st:spaces(st)+str(st))(A[i][j]) for j in range(n)))

def check_leftdown(A,h,w,n):
	h,w = ((lambda h,w: (h,x) if A[x][w-1]==0 else (h,w-1))(*((h,w-1) if h+1>n-1 else (h+1,w-1))) ) if h+1>n-1 else (
		(lambda h,w: (h+1,0) if w-1<0 else (h+1,w-1))(h,w)
	)
	if h+1>n-1 and w<0: w=n-1
	return h,w

def check_rightdown(A,h,w,n):
	import operator as op
	if h+1>n-1:
		if w+1>n-1: pass
		else:
			w+=1
		h = next((x for x in range(n) if A[x][w]==0),h)
	else:
		if w+1>n-1:
			h+=1
			w=0
		else:
			h+=1
			w+=1
			if A[h][w]!=0: h,w=check_leftdown(A,h,w,n)
	return h,w

if __name__ == '__main__':
	import sys
	from itertools import count, dropwhile
	def readints():
		for line in sys.stdin:
			if line.strip():
				yield int(line)
	it = readints()
	for n in dropwhile(lambda x:x!=0,it):
		try:
			if n==0: break
			A=[[0]*n for _ in range(n)]
			cnt=n*n
			mid=n//2
			h,w=mid+1,mid
			A[h][w]=1
			for x in range(2,cnt+1):
				h,w=check_rightdown(A,h,w,n)
				A[h][w]=x
			print_board(A,n)
		except Exception: break