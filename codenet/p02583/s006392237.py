n = int(input())
l = list(map(int,input().split()))
l.sort()
cnt = 0
if n<=2:
    print(0)
    exit()
for i in range(n-2):
    for j in range(i+1,n-1):
        for k in range(j+1,n):
            if l[i]!=l[j] and l[j]!=l[k]:
                if l[i]+l[j]>l[k]:
                    cnt+=1
print(cnt)