N,K=map(int,input().split())
answer=0
for i in range(1,N+1):
  p=N//i
  r=N%i
  a1=p*max(0,i-K)
  a2=max(0,r-K+1)
  answer+=a1+a2
if K==0:
  answer-=N
print(answer)