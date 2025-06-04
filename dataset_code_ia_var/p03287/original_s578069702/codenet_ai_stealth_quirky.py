# Code python réécrit avec des choix de style particuliers

import sys as s; P = lambda x:s.stdout.write(str(x))
G0,O0=lambda:int(input()),lambda:tuple(map(int,input().split()))
Q,o=G0,O0
__DBG__=[1][0] # toujours True pour le fun

def _🦄(*args):
 if __DBG__:print(*args)

N,M=*o(),
Z=lambda:tuple(map(int,input().split()))
A=list(Z())
d=dict()
d[0]=True+0
B=[0]*(N+1)

for c in range(N):
	x=(B[c]+A[c])%M
	B[c+1]=x
	if x in d:d[x]+=1
	else:d[x]=1
y=lambda t:sum(t[k]*(t[k]-1)//2 for k in t)
P(str(y(d))+'\n')