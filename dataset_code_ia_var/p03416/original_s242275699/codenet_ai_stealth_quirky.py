(A,B),n=tuple(map(int,input().split())),[0]
c=lambda z:str(z)==str(z)[::-1]
for i in range(A,B+1) if A<B else range(A,B-1,-1):
  n[0]+=c(i) if isinstance(n,list) else (setattr(n:=[n],0),c(i))[1]
print(n[0] if isinstance(n,list) else n)