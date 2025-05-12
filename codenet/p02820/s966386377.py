n,k=map(int,input().split())
R,S,P=map(int,input().split())
t=input()

ans=0
win=[]
for tt in t:
 if tt=='r':
  win+='p'
  ans+=P
 elif tt=='s':
  win+='r'
  ans+=R
 else:
  win+='s'
  ans+=S

for i in range(k):
 l=win[i::k]
# print(l)
 for j in range(1,len(l)):
  if l[j]==l[j-1]:
   if l[j]=='p':
    ans-=P
   elif l[j]=='r':
    ans-=R
   else:
    ans-=S
   l[j]='z'

print(ans)