n,c=list(map(int,input().split()))
pli=list(map(int,input().split()))
for i in range(c):
    p=sum(pli)
mycake=p//(n+1)
if p%(n+1)>0:mycake+=1
print(mycake)