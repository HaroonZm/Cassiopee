def gcd(a,b):
	return a if b==0 else gcd(b,a%b)
	
while 1:
	a1,m1,a2,m2,a3,m3=map(int,raw_input().split())
	if a1==0:break
	x=y=z=1
	x=a1*x%m1
	y=a2*y%m2
	z=a3*z%m3
	cx=cy=cz=1
	while x!=1:
		x=a1*x%m1
		cx+=1
	while y!=1:
		y=a2*y%m2
		cy+=1
	while z!=1:
		z=a3*z%m3
		cz+=1
	lcd=cx*cy/gcd(cx,cy)
	lcd=lcd*cz/gcd(lcd,cz)
	print lcd