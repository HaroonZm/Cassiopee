s=input()
n=len(s)
def valid(seg):
    if len(seg)==0 or (seg[0]=='0' and len(seg)>1) or int(seg)>255:
        return False
    return True
res=0
for i in range(1,min(4,n-2)):
    for j in range(i+1,min(i+4,n-1)):
        for k in range(j+1,min(j+4,n)):
            a,b,c,d=s[:i],s[i:j],s[j:k],s[k:]
            if all(map(valid,[a,b,c,d])):
                res+=1
print(res)