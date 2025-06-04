def get_icicles():
    lst = []
    first_line = input().strip().split()
    n=int(first_line[0])
    l=int(first_line[1])
    for _ in range(n):
        val=int(input() . strip())
        lst.append(val)
    class ReturnVals: pass
    ret=ReturnVals()
    ret.icicles,ret.N,ret.L=lst,n,l
    return ret

def do_diff(arr, sz):
    # imperative + functional style mixed
    res = []
    for i, v in enumerate(arr):
        right = (arr[i+1] - v) if i!=(sz-1) else -v
        left = (v - arr[i-1]) if i!=0 else v
        right = 1 if right>0 else -1
        left = 1 if left>0 else -1
        check = right - left
        res.append(0 if not check else (1 if check > 0 else -1))
    return res

info = get_icicles()
icicles, N, L = info.icicles, info.N, info.L

difference = do_diff(icicles, N)

times = [-1 for _ in range(N)]
peaks = []
for i in range(N):
    if difference[i]==-1:
        peaks.append(i)

def peak_op(idx, time_ref, icicles, L, diff, N):
    t = L - icicles[idx]
    time_ref[idx]=t
    is_left=False; is_right=False
    pl=idx; pr=idx
    while (not is_left) or (not is_right):
        pl-=1
        if pl<0:
            is_left=True
        if not is_left:
            if time_ref[pl]==-1:
                time_ref[pl]=(L-icicles[pl])+time_ref[pl+1]
            else:
                time_ref[pl]=(L-icicles[pl])+max(time_ref[pl-1],time_ref[pl+1])
            if diff[pl]==1:
                is_left=True
        pr+=1
        if pr>=N:
            is_right=True
        if not is_right:
            if time_ref[pr]==-1:
                time_ref[pr]=(L-icicles[pr])+time_ref[pr-1]
            else:
                time_ref[pr]=(L-icicles[pr])+max(time_ref[pr-1],time_ref[pr+1])
            if diff[pr]==1:
                is_right=True

for idx in peaks:
    peak_op(idx, times, icicles, L, difference, N)

maximum = None
for t in times:
    if maximum is None or t > maximum:
        maximum = t
print(maximum)