x=int(input())
ans=x//11*2
x%=11
if x>0 and x<7:
  ans+=1
if x>6:
  ans+=2
print(ans)