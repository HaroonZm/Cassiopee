def fact(n):
	return 1 if n == 0 else n*fact(n-1)

S = raw_input()
lS,ls = len(S),len(set(list(S)))
d = [S.count(i) for i in set(list(S))]
dd = sum([d[i]%2 for i in range(ls)])
if (lS%2 == 0 and dd != 0 )or (lS%2 == 1 and dd != 1): 
		print 0
else:
	denomi = 1
	for i in range(ls):
		denomi *= fact(d[i]/2)
	print fact(lS/2)/denomi