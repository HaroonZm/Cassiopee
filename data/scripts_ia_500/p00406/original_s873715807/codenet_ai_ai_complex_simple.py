from functools import reduce
N,L=map(int,input().split())
c=sorted(reduce(lambda a,x:a+[(x[0],x[1])],(map(int,input().split())for _ in[0]*N),[]))
masu=list(map(lambda t:t[0],c))
dir=list(map(lambda t:t[1],c))
score,result=0,float('-inf')

def update_score(idx,score):
    return (score+(masu[idx]-idx-1) if dir[idx]==0 else score-(masu[idx]-idx-1))
score=reduce(lambda s,j:update_score(j,s),range(N),score)
masu=list(map(lambda j:j+1,range(N)))
result=score

for i in range(N-1,-1,-1):
    delta = (L-(N - i) - masu[i] + 1)
    if dir[i]==1: score+=delta
    else: score-=delta
    masu[i]=L-(N - i)+1
    result=max(result,score)
print(result)