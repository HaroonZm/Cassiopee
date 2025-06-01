N=int(input())
L=list(map(int,input().split()))
M=[0 for _ in range(N)]
i=0
while i<N:
  if M[i]==0:
    V=set()
    p=i
    flag=True
    while p not in V:
      if M[p]==1:
        flag=False
        break
      V.add(p)
      M[p]=1
      p=(p+L[p])%N
    if flag:
      while M[p]==1:
        M[p]=2
        p=(p+L[p])%N
  i+=1
print(sum(x==2 for x in M))