import re
while 1:
	n,m = map(int,raw_input().split())
	if n == m == 0: break
	R = [0]*n
	for i in range(n):
		p,s,d = raw_input().replace("?","[0-9]").split()
		R[i] = [re.compile(s+d), p[0] == "p"]
	ans = []
	for i in range(m):
		s,d,name = raw_input().split()
		for r,p in R[::-1]:
			if r.search(s+d):
				if p: ans.append([s,d,name])
				break
	print len(ans)
	for s,d,name in ans:
		print s,d,name