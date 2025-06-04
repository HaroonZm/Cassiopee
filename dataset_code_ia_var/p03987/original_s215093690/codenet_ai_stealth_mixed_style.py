N=int(input())
As=[int(x) for x in input().split()]

def build_index(arr):
    arr_idx=[0]*(len(arr)+1)
    for idx,val in enumerate(arr):
        arr_idx[val]=idx
    return arr_idx

iAs = build_index(As)
result=0

iLs = list((lambda n: [x for x in range(n+1)])(N))
iRs = [x for x in range(N+1)]

for a in (lambda: reversed(range(1,N+1)))():
    ia = iAs[a]
    il = iLs[ia]
    ir = iRs[ia]
    result += a * (ia - il + 1) * (ir - ia + 1)
    iLs[ir+1 if ir+1<=N else N] = il
    if il-1>=0:iRs[il-1]=ir

print(result)