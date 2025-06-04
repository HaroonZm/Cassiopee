n=int(input())
files=[input().split() for _ in range(n)]
files=[(d,l) for d,l in files]

res=0
i=0
while i<n:
    if files[i][0]=='y':
        res+=1
        j=i+1
        while j<n and files[j][0]!='n':
            j+=1
        i=j
    else:
        i+=1
print(res)