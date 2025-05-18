n,t,e = map(int,raw_input().split())
x = map(int,raw_input().split())
for i in range(n):
	r = t%x[i]
	if min(r, x[i] - r) <= e:
		print i+1
		break
else:
	print -1