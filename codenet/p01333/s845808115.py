while True:
  a,b= map(int,raw_input().split())
  if a== 0 and b ==0: break
  c=b-a
  ans,ans2,ans3=0,0,0
  while c>=1000:
    c-=1000
    ans+=1
  while c>=500:
    c-=500
    ans2+=1
  while c>=100:
    c-=100
    ans3+=1
  else:
    print ans3,ans2,ans