s=input()
sl=len(s)
ans=0
for i in range(2**(sl-1)):
    bit=bin(i)[2:].zfill(sl-1)
    now=0
    for j in range(len(s)-1):
        if int(bit[j]):
            ans+=int(s[now:j+1])
            now=j+1
    ans+=int(s[now:])
print(ans)