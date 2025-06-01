N=int(input())
A=[]
for _ in range(0,N):
	a=list(map(int,input().split()))
	a.sort()
	if A.count(a)==0:
		A.append(a)

print(N-len(A))