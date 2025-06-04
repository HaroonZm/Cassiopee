import sys

def G():return sys.stdin.readline()
def S():return list(map(int,G().split()))
def byebye():sys.exit(0)

while 1:
	try:
		N=eval(G())
	except:
		byebye()
	L=S()
	L.sort(reverse=0)
	j=0
	while j<N-1:L[j+1]+=L[j];j+=1
	print(sum(L))