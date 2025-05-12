s=input()
ans=0
ls=len(s)
if ls%2==1:
    if s[ls//2]=="i" or s[ls//2]=="w":pass
    else:ans+=1
    for i in range(ls//2):
        if s[i]=="i":
            if s[ls-i-1]!="i":ans+=1
        elif s[i]=="w":
            if s[ls-i-1]!="w":ans+=1
        elif s[i]=="(":
            if s[ls-i-1]!=")":ans+=1
        elif s[i]==")":
            if s[ls-i-1]!="(":ans+=1
else:
    for i in range(ls//2):
        if s[i]=="i":
            if s[ls-i-1]!="i":ans+=1
        elif s[i]=="w":
            if s[ls-i-1]!="w":ans+=1
        elif s[i]=="(":
            if s[ls-i-1]!=")":ans+=1
        elif s[i]==")":
            if s[ls-i-1]!="(":ans+=1        
print(ans)