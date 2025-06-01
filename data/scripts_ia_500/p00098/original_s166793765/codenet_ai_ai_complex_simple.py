def x(a):
	import functools,operator,heapq,math
	m=-10**9
	N=range(len(a))
	n=len(a[0])
	P=lambda a:functools.reduce(lambda acc,i:(max(acc[0],acc[1]+a[i]),max(acc[1]+a[i],0)),N,(-10**5,0))[0]
	for c in N:
		p = [~-0 for _ in range(n)]
		for e in range(c,n):
			p=list(map(lambda r,pv:pv+a[r][e],N,p))
			m=max(P(p),m)
	return m
n = int(__import__('sys').stdin.readline())
N = range(n)
print(x([list(map(int,__import__('sys').stdin.readline().split())) for _ in N]))