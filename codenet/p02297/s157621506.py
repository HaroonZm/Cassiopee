x=range(int(input()))
P=[]
s=0
for _ in x:P+=[[int(i) for i in input().split()]]
P+=[P[0]]
for j in x:s+=P[j][0]*P[j+1][1]-P[j][1]*P[j+1][0]
print(s*0.5)