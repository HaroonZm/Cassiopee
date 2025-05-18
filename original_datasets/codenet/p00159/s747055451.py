def bmi(a):
	a=map(int,a.split())
	return a[0], abs(22-a[2]/((a[1]/100.0)**2))
	
while 1:
	n=input()
	if n==0:break
	print sorted(sorted([bmi(raw_input()) for i in range(n)]),key=lambda x:x[1])[0][0]