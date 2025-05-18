h, w, k=map(int, input().split())
table=list(input() for i in range(h))

ans=0
cnt=0

for i in range(2**h):
    for j in range(2**w):
        for s in range(h):
            for t in range(w):
                if table[s][t]=="#" and (i>>s)&1 and (j>>t)&1:
                    cnt+=1
        
        if cnt==k:
            ans+=1

        cnt=0
print(ans)