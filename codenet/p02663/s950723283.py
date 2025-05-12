H1, M1, H2, M2, K= map(int,input().split())
ans=H2-H1
ans*=60
ans+=M2-M1
ans+= -K
if ans <0:
  ans=0
print(ans)