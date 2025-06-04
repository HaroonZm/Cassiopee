import sys
input=sys.stdin.readline

while True:
    N,M=map(int,input().split())
    if N==0 and M==0:
        break
    s=list(map(int,input().split()))
    d=list(map(int,input().split()))
    # sum_s: total warmth sum of all futons
    sum_s=sum(s)
    # count how many futons have each warmth
    from collections import Counter
    c=Counter(s)
    items=list(c.items())
    # DP:
    # dp[i][sum] = minimal discomfort using first i types of futons to get sum warmth on the bed day by day
    # We want to find sequence f_j (sum of bed futon warmth each day) minimizing sum |f_j - d_j|
    #
    # Since order in closet can be rearranged arbitrarily, the futons stack order is flexible.
    # We only care about the number of futons on bed each day (and which ones) since adding/removing futons one by one simulates adding/removing top futon in closet.
    #
    # We perform DP for each subset sum of futons warmth, then do DP over days for best cumulative discomfort
    
    max_sum = sum_s
    dp_subset = [False]*(max_sum+1)
    dp_subset[0]=True
    for v,count in items:
        ndp = dp_subset[:]
        for _ in range(count):
            for val in range(max_sum-v,-1,-1):
                if dp_subset[val]: ndp[val+v]=True
        dp_subset=ndp
    
    possible_sums = [i for i,b in enumerate(dp_subset) if b]
    
    # f_j for day j must be in possible_sums (sum of chosen futons)
    # DP over days and possible sums:
    # dp_day[i][sum]= minimal total discomfort after day i with bed warmth sum
    INF=10**15
    dp_day = [INF]*(max_sum+1)
    # day 0 no futons on bed
    dp_day[0]=0
    
    for day in range(M):
        ndp_day = [INF]*(max_sum+1)
        for sum_warmth in possible_sums:
            cost = dp_day[sum_warmth]
            if cost == INF:
                continue
            for nxt in possible_sums:
                # moving futons changes bed from sum_warmth to nxt is always possible by pushing/popping top futons from closet
                ndp_day[nxt] = min(ndp_day[nxt], cost + abs(nxt - d[day]))
        dp_day=ndp_day
    print(min(dp_day))