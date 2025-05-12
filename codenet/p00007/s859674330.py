a=100000
j=int(input())
for i in range(j):
	a*=1.05
	if a%1000==0:
		pass
	else:
		a=(a+1000)-a%1000
print(int(a))