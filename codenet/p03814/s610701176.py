s=input()
l=len(s)
a=[]
z=[]
ans=0
for i in range(l):
    if s[i]=="A":
        a.append(i)
    elif s[i]=="Z":
        z.append(i)

ans=(max(z)-min(a)+1)

print(ans)