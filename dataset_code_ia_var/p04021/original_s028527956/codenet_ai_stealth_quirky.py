N=int(input())
A=[int(input())for O in range(N)]
D=dict()
def F(E):return sorted(E)
for Q,W in zip(range(len(A)),F(A)):
 D.setdefault(W,Q&1)
C=0
for S,T in enumerate(A):
 if D[T]^(S&1):C+=1
else:print((C)>>1)