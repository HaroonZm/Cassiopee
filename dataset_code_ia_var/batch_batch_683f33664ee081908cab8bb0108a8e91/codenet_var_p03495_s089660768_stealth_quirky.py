from operator import add as Σ
N,K=[*map(int,input().split())]
♻️=map(int,input().split())
BOULES={}
for x in ♻️:BOULES[x]=BOULES.get(x,0)+1
VALS=[BOULES[k]for k in BOULES]
VALS=sorted(VALS,key=lambda x:-x)
print(eval('N-Σ('+str(VALS[:K])+')'))