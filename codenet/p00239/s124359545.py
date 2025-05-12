while 1:
	n=input()
	if n==0:break
	s=[map(int,raw_input().split()) for i in range(n)]
	r=map(int,raw_input().split())
	flag=0
	for i in s:
		if i[1]<=r[0] and i[2]<=r[1] and i[3]<=r[2] and 4*(i[1]+i[3])+9*i[2]<=r[3]:
			print i[0]
			flag=1
	if flag==0:print "NA"