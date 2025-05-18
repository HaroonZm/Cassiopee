M=4294967311

def pmod(v):
	return (v%M+M)%M

def mpow(x,N):
	res=1
	while (N>0):
		if(N%2):
			res=pmod(res*x)
		x=pmod(x*x)
		N/=2
	return res

def minv(a):
	return mpow(a,M-2)

N=input()
v=0
for i in range(N):
	c,y=map(int,raw_input().split())
	if (c==1):
		v=pmod(v+y)
	if (c==2):
		v=pmod(v-y)
	if (c==3):
		v=pmod(v*y)
	if (c==4):
		v=pmod(v*minv(y))

if (v<(1<<31)):
	v=v
else:
	v=v-M;

print "%d" % v