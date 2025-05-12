n=int(input())
l=list(map(int,input().split()))

counter=0
for i in range(n):
    minimum=i
    for j in range(i,n):
        if l[minimum]>l[j]:
            minimum=j
    if i!=minimum:
        l[minimum],l[i]=l[i],l[minimum]
        counter+=1
print(*l)
print(counter)