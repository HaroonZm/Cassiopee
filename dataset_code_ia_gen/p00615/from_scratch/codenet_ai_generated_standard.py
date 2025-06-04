while True:
    n,m=map(int,input().split())
    if n==0 and m==0:
        break
    tl=[]
    if n>0:
        tl=list(map(int,input().split()))
    tr=[]
    if m>0:
        tr=list(map(int,input().split()))
    times=sorted(tl+tr)
    if not times:
        print(0)
        continue
    max_gap=times[0]-0
    for i in range(1,len(times)):
        gap=times[i]-times[i-1]
        if gap>max_gap:
            max_gap=gap
    end=times[-1]
    if end>max_gap:
        max_gap=max(max_gap,end)
    print(max_gap)