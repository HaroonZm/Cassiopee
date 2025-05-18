n=input()
m=input()
ks=[input() for i in range(m)]
card=[v for v in range(1,n*2+1)]
for k in ks:
    if k==0:
        tmp=[]
        c1,c2=card[:n],card[n:]
        for i in range(n):
            tmp+=[c1[i],c2[i]]
        card=tmp
    else:
        card=card[k:]+card[:k]

for v in card:
    print v