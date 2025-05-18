x=range(int(input()))
P=[]
for _ in x:P+=[[int(i) for i in input().split()]]
_=0
P+=[P[0]]
for j in x:
    k = j+1
    _+=P[j][0]*P[k][1]-P[j][1]*P[k][0]
print(_*0.5)