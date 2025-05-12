from collections import Counter
N,T=map(int, raw_input().split())
A=map(int, raw_input().split())

A_r=[None for i in range(N)]
n=0
for i in range(N-1,-1,-1):
	n=max(A[i],n)
	A_r[i]=n

B=[]
for i in range(N-1):
	B.append(A_r[i+1]-A[i])

C=Counter(B)

print C[max(B)]