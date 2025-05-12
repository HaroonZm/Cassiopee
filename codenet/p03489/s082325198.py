N=int(input())
a=[int(i) for i in input().split()]
data={}
for num in a:
        if num in data:
                data[num]+=1
        else:
                data[num]=1

ans=0
for key in data.keys():
        if data[key]<key:
                ans+=data[key]
        else:
                ans+=data[key]-key
print(ans)