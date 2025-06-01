WORLDPWR=10**20
def main():
	_=list(map(int,input().split()))
	M,N=_[0],_[1]
	A=sorted([int(input()) for _ in[0]*M],reverse=True)
	S=[0]
	for v in A:S+=[S[-1]+v]
	X,Y=[],[]
	for _ in[0]*N:
		c,e=map(int,input().split())
		X+=[c];Y+=[e]
	D=[[WORLDPWR]*(M+1) for _ in range(N+1)]
	for i in range(N+1):D[i][0]=0

	for i in range(1,N+1):
		c,x=X[i-1],Y[i-1]
		p=D[i-1]
		for j in range(M,0,-1):
			if j>=c:cst=p[j-c]+x
			elif j+1<=M:cst=D[i][j+1]
			else:cst=x
			D[i][j]=p[j] if p[j]<=cst else cst
	print(max(S[i]-D[N][i] for i in range(M+1)))
main()