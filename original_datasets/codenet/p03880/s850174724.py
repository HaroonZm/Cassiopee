n=int(raw_input())
a=[int(raw_input()) for _ in xrange(n)]
mxlba=0
for i in xrange(n):
    mxlba=max(mxlba,len(bin(a[i])[2:]))

exist=[False]*(mxlba+1000)
for i in xrange(n):
    bit=bin(a[i])[2:]
    lb=len(bit)
    for j in xrange(lb-1,-1,-1):
        if bit[j]=="1":
            exist[lb-1-j]=True
            break

axor=0
for i in xrange(n):
    axor^=a[i]
if axor==0:
    print(0)
    exit()
axor=bin(axor)[2:]
la=len(axor)
ans=0
i=0
while i<la:
    if axor[i]=="1":
        if not exist[la-i-1]:
            print(-1)
            exit()
        else:
            ans+=1
            if la-i-1==0:
                break
            tmp=int("1"*(la-i-1),2)
            axor=int(axor,2)^tmp
            axor=bin(axor)[2:]
    i+=1

print(ans)