N=int(input())
alist=list(map(int,input().split()))

avg=sum(alist)/N
min_index=-1
min_diff=1000
for i in range(N):
  diff=abs(avg-alist[i])
  if diff<min_diff:
    min_diff=diff
    min_index=i
    
print(min_index)