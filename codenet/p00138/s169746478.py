O=[]
dic={}
for i in range(3):
    d={}
    for j in range(8):
        n,t=map(float,raw_input().split())
        d[t]=int(n)
    ls=sorted(d)
    for j in ls[:2]:
        O.append((d[j],j))
    for j in ls[2:]:
        dic[j]=d[j]
for i in sorted(dic)[:2]:
    O.append((dic[i],i))
for i in O:
    print i[0],i[1]