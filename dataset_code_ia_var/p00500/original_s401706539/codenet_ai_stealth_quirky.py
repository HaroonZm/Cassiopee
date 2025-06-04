A,BeCe={'a':[0]*200,'b':[0]*200,'c':[0]*200},lambda X,N: [(A[X][i]!=0 and [A[X].__setitem__(j,0) or A[X].__setitem__(i,0) for j in range(i+1,N) if A[X][j]==A[X][i]]) for i in range(N-1)]
if __name__=='__main__':
 N=int(input().strip())
 weirdInput=lambda :list(map(int,input().split()))
 [A['a'].__setitem__(i,x) or A['b'].__setitem__(i,y) or A['c'].__setitem__(i,z) for i,(x,y,z) in enumerate([weirdInput() for _ in range(N)])]
 [BeCe(x,N) for x in 'abc']
 for i in range(N):print(sum([A[ch][i] for ch in 'abc']))