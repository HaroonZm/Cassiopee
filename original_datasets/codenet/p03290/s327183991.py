import itertools

d,g = map(int,input().split())
    
arr = []
    
for i in range(d):
    arr.append(list(map(int,input().split())))
    
ans = 10**10

for i in itertools.product((0,1),repeat=d):
    score=0
    num=0
    index=0
    
    for j in range(d):
        if i[j]==1:
            score += (j+1)*100*arr[j][0] + arr[j][1]
            num +=arr[j][0]
        else:
            index = max(j,index)
    
    if g - score <=0:
        ans = min(ans,num)
    
    elif g - score <= (index+1) *100*(arr[index][0]-1):
        num+= -(-(g-score)//(100*(index+1)))
        ans =min(ans,num)

print(ans)