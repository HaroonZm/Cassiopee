for j in [1]*input():
	n=input()
	a=map(int,raw_input().split())
	l=[a[i+1]-a[i] for i in range(n-1)]
	print max(0,max(l)),-min(-0,min(l))