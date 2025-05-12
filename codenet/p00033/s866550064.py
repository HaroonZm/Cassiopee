def s(a):
	b=c=0
	for i in a:
		if   i>b:b=i
		elif i>c:c=i
		else:return 0
	return 1
for n in range(int(raw_input())):
	print "YES" if s(map(int,raw_input().split())) else "NO"