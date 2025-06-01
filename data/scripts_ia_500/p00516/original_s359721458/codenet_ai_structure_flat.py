n,k=map(int,raw_input().split())
a=[]
for i in range(n+k):
    a.append(input())
cnt={}
for i in range(n):
    cnt[i]=0
for i in range(n,n+k):
    for j in range(n):
        if a[i]>=a[j]:
            cnt[j]+=1
            break
max_count=-1
max_index=-1
for key in cnt:
    if cnt[key]>max_count:
        max_count=cnt[key]
        max_index=key
print(max_index+1)