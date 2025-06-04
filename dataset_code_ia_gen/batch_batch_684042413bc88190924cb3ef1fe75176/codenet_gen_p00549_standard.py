N=int(input())
S=input()
countJ=[0]*(N+2)
countI=[0]*(N+2)
for i in range(1,N+1):
    countJ[i]=countJ[i-1]+(1 if S[i-1]=='J' else 0)
for i in range(N,0,-1):
    countI[i]=countI[i+1]+(1 if S[i-1]=='I' else 0)
res=0
for pos in range(N+1):
    for c in 'JOI':
        mid=1 if c=='J' else (2 if c=='O' else 3)
        if c=='J':
            tmp = countJ[pos]
            tmp *= countI[pos+1]
        elif c=='O':
            tmp=0
            for j in range(pos):
                if S[j]=='J':
                    for k in range(pos,N):
                        if S[k]=='I':
                            tmp+=1
        else:
            tmp=0
            for j in range(pos):
                if S[j]=='J':
                    for k in range(pos,N):
                        if S[k]=='I':
                            tmp+=1
        if c=='J':
            tmp = countJ[pos]*countI[pos+1]
        elif c=='O':
            tmp=0
            for i1 in range(pos):
                if S[i1]=='J':
                    tmp += countI[pos+1]
        else:
            tmp= countJ[pos]*countI[pos+1]
        if c=='J':
            tmp=countJ[pos]*countI[pos+1]
        elif c=='O':
            tmp=0
            cntJ=0
            for i1 in range(pos):
                if S[i1]=='J':
                    cntJ+=1
            cntI=0
            for i2 in range(pos,N):
                if S[i2]=='I':
                    cntI+=1
            tmp=cntJ*cntI
        else:
            tmp=countJ[pos]*countI[pos+1]
        res=max(res,tmp)
print(res)