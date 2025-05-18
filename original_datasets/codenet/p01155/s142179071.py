import math
while(1):
    [a,b]=[int(x) for x in raw_input().split()]
    if a==0:
        break
    else:
        anum=[]
        bnum=[]
        ruinmin=10000**2*3
        for i in range(1,101):
            if a%i==0 and math.sqrt(a)>=i:
                anum.append([i,a/i])
            if b%i==0 and math.sqrt(b)>=i:
                bnum.append([i,b/i])
        for apair in anum:
            for bpair in bnum:
                abset=sorted(apair+bpair)
                ruin=(abset[1]-abset[0])**2+(abset[2]-abset[1])**2+(abset[3]-abset[2])**2
                ruinmin=min(ruinmin,ruin)
        print ruinmin# your code goes here