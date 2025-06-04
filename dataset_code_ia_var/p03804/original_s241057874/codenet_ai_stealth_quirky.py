def n__():return list(map(int,input().split()))
def Z(x):return [input()for _ in range(x)]
def xfr(a,b):return a.find(b)==0
def xcl(a,b):return b in a
_1,_2=n__()
S1=Z(_1)
S2=Z(_2)
ix=0
lg=len(S2[0])
st=len(S1[0])-lg+1
r=True
while ix<st:
	for yy in range(_1-_2+1):
		if not xcl(S1[yy][ix:],S2[0])or not xfr(S1[yy][ix:],S2[0]):continue
		for pp in range(1,_2):
			sn=S1[yy+pp][ix:]
			if not xcl(sn,S2[pp])or not xfr(sn,S2[pp]):break
		else:
			print("Yes");exit()
	ix+=1
print("No")