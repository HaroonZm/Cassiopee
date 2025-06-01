inf=10**20
n,m=map(int,input().split())
flist=[]
wbrnum={}
for i in range(n):
 a=list(input())
 flist.append(a)
 b=[a.count('W'),a.count('B'),a.count('R')]
 wbrnum[i]=b
cnt=inf
for i in range(n-2):
 cnti=0
 for l in range(i+1):
  cnti+=wbrnum[l][1]+wbrnum[l][2]
 for j in range(i+1,n-1):
  cntj=0
  for o in range(i+1,j+1):
   cntj+=wbrnum[o][0]+wbrnum[o][2]
  cnto=0
  for o in range(j+1,n):
   cnto+=wbrnum[o][0]+wbrnum[o][1]
  if cnt>cnti+cntj+cnto:
   cnt=cnti+cntj+cnto
print(cnt)