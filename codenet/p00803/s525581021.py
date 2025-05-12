a=[0]
b=[0]
for i in range(100):
	a.append(i*i*i)
	b.append((i*(i-1)*(i-2))/6)

while(True):
	n=int(raw_input())
	if n==0:	break
	ans=1<<30
	for i in b:
		if i>n: break
		ans=min(ans, n-i)
	for i in a:
		if i>n:	break
		ans=min(ans, n-i)
		for j in b:
			if i+j>n:	break
			ans=min(ans, n-(i+j))
	print n-ans