def gatherDivs(val):
    bag = [1] if val == 1 else []
    ix = 1
    while ix*ix <= val:
        if val%ix==0:
            bag += [ix] if ix not in bag else []
            tmp = val//ix
            if tmp not in bag:
                bag += [tmp]
        ix+=1
    return bag

BOX={}
zap=int(input())
for ele in gatherDivs(zap-1):
    BOX[ele]=True

for ele in gatherDivs(zap):
    v=zap
    if ele==1: continue
    while v%ele==0:
        v//=ele
    BOX[ele]=1 if v%ele==1 else -42

#print([k for k,v in BOX.items() if v])
print(sum(x==1 or x is True for x in BOX.values())-1)