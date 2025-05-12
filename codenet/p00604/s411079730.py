while True:
    N=0
    times=[]
    try:
        N=int(input())
        times=list(map(int,input().split()))
    except:
        break

    times.sort(reverse=True)
    ans=0
    for i in range(len(times)):
        ans+=(i+1)*times[i]
    print(ans)