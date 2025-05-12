while 1:
    D,W=list(map(int,input().split()))
    if (D,W)==(0,0):
        break
    garden = [list(map(int,input().split())) for _ in range(D)]
    ans=0
    for wi in range(W):
        for wj in range(wi+2,W):
            for di in range(D):
                for dj in range(di+2,D):
                    edge_min = float("inf")
                    water_sum=0
                    count=0
                    in_max=0
                    for w in range(wi,wj+1):
                        for d in range(di,dj+1):
                            if w in (wi,wj) or d in (di,dj) :
                                edge_min= min(garden[d][w] , edge_min)
                                ###print(edge_min,garden[d][w],"eee",min(edge_min,garden[d][w]))
                            else:
                                water_sum+=garden[d][w]
                                in_max=max(in_max,garden[d][w])
                                count+=1
                    if edge_min>in_max:                    
                        ans=max(ans,edge_min*count - water_sum)
    print(ans)