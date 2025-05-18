S=input()
l=int(len(S))
k=0
p=[0]*10
for i in range(l):
    if S[i]=="A" or S[i]=="G" or S[i]=="C" or S[i]=="T" :
        k+=1
        p[i]=k
    else:
        k=0
        p[i]=k
ans=max(p[0],p[1],p[2],p[3],p[4],p[5],p[6],p[7],p[8],p[9])
print(ans)