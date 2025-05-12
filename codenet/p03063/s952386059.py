N=int(input())
S=input()

allblack=0
for i in range(N):
  if S[i]!='#':
    allblack+=1
    
answer=allblack
whitecount=allblack   
blackcount=0

for i in range(N):
  if S[i]=='.':
    whitecount-=1
  else:
    blackcount+=1
  tmp=blackcount+whitecount
  answer=min(answer,tmp)
  
print(answer)