def x(a):
	m=-10**9
	for c in N:
		p=[0]*n 
		for e in range(c,n):
			for r in N:
				p[r]+=a[r][e]
			m=max(P(p),m)
	return m
def P(a):
	m,c=-10**5,0
	for i in N:
		c+=a[i]
		m=max(c,m)
		if c<0:c=0
	return m
n = input()
N = range(n)
print x([map(int, raw_input().split()) for i in N])