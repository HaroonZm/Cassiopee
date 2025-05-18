n=int(input())
nlist=list(map(int,input().split()))
abslist=[]

for i in range(n-1) :
  abslist.append(abs(sum(nlist[:i+1])-sum(nlist[i+1:])))

print(min(abslist))