D=int(input())
c=list(map(int,input().split()))
s=[]
t=[]
v=0
lastday=[0 for i in range(26)]

for i in range(D):
  tmp=list(map(int,input().split()))
  s.append(tmp)
for i in range(D):
  tmp=int(input())-1
  t.append(int(tmp))

for i in range(1,D+1):
  v+=s[i-1][t[i-1]]
  lastday[t[i-1]]=i
  for j in range(26):
    v-=c[j]*(i-lastday[j])
  print(v)