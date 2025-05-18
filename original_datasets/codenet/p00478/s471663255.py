s=raw_input()
n=input()
ans=0
for i in range(n):
    r=raw_input()
    for j in range(len(r)):
        flag=True
        for k in range(len(s)):
            ri=(j+k)%len(r)
            if r[ri]!=s[k]:
                flag=False
        if flag:
            ans+=1
            break
print ans