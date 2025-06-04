N=int(input())
r=list(map(int,input().split()))
units=[tuple(map(int,input().split())) for _ in range(N)]
def get_scores(vals):
    arr=[(v,i) for i,v in enumerate(vals)]
    arr.sort(key=lambda x:-x[0])
    scores=[0]*N
    i=0
    while i<N:
        j=i+1
        while j<N and arr[j][0]==arr[i][0]:
            j+=1
        for k in range(i,j):
            scores[arr[k][1]]=r[i]
        i=j
    return scores
def total_scores(units):
    s_scores=get_scores([u[0] for u in units])
    p_scores=get_scores([u[1] for u in units])
    c_scores=get_scores([u[2] for u in units])
    return [s+p+c for s,p,c in zip(s_scores,p_scores,c_scores)]
def rank(scores):
    sorted_scores=sorted(set(scores),reverse=True)
    ranks=[sorted_scores.index(x)+1 for x in scores]
    return ranks
base_scores=total_scores(units)
base_rank=rank(base_scores)[0]
if base_rank<=8:
    print(0)
    exit()
res=None
for idx in range(3):
    vals=[u[idx] for u in units]
    D=[]
    for i,v in enumerate(vals[1:],start=1):
        if v>vals[0]:
            D.append(v-vals[0])
    D.append(1)
    D=list(sorted(set(D)))
    for d in D:
        new_vals=[]
        for i,u in enumerate(units):
            if i==0:
                nv=list(u)
                nv[idx]+=d
                new_vals.append(tuple(nv))
            else:
                new_vals.append(u)
        scores=total_scores(new_vals)
        ranks=rank(scores)
        if ranks[0]<=8:
            if res is None or d<res:
                res=d
            break
print(res if res is not None else "Saiko")