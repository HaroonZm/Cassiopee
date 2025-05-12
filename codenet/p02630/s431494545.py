N=int(input())
A=list(map(int,input().split()))
dic={}
for i in range(N):
  if(A[i] not in dic):
    dic[A[i]]=1
  else:
    dic[A[i]]+=1
Q=int(input())
s=sum(A)
for i in range(Q):
  B,C=list(map(int,input().split()))
  t=dic.get(B,0)
  s=s - t*B
  s=s + t*C
  print(s)
  if(C in dic):
    dic[C]+=t
  else:
    dic[C]=t
  dic[B]=0