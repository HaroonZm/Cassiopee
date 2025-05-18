t=input()
p=input()
mae=[0]*len(p)
cnt=0
for i in range(len(t)):
    if t[i]==p[cnt]:
        mae[cnt]=i
        cnt+=1
        if cnt==len(p):
            break
if cnt!=len(p):print("no");exit()
cnt-=1
for j in range(len(t)-1,-1,-1):
    if t[j]==p[cnt]:
        if mae[cnt]!=j:print("no");exit()
        cnt-=1
    if cnt==-1:break
if cnt!=-1:print("no")
else:print("yes")