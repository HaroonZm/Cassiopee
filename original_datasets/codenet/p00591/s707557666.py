while 1:
	n=input()
	if n==0:break
	s=[map(int,raw_input().split()) for i in range(n)]
	sh=set([min(s[i]) for i in range(n)])
	tl=set([max([s[j][i] for j in range(n)]) for i in range(n)])
	print list(sh&tl)[0] if len(sh&tl)>0 else 0