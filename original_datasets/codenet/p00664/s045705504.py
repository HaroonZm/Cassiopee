import bisect
while 1:
	r,c,q = map(int,raw_input().split())
	if r == 0: break
	R = [[0,0] for i in range(r)]
	C = [[0,0] for i in range(c)]
	for i in range(1,q+1):
		A,B,order = map(int,raw_input().split())
		if A == 0:
			R[B] = [i,order]
		else:
			C[B] = [i,order]
	c1 = sorted(C[ci][0] for ci in range(c) if C[ci][1] == 1)
	c0 = sorted(C[ci][0] for ci in range(c) if C[ci][1] == 0)
	ans = r*sum(C[ci][1] for ci in range(c))
	for ri in range(r):
		if R[ri][1] == 0:
			ans -= bisect.bisect(c1,R[ri][0])
		else:
			ans += bisect.bisect(c0,R[ri][0])
	print ans