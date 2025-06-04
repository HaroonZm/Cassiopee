import sys
from collections import deque
input=sys.stdin.readline

N,M,W,T=map(int,input().split())
items=dict()
for _ in range(M):
    s,v,p=input().split()
    v=int(v)
    p=int(p)
    items[s]=(v,p)
markets=[]
for _ in range(N):
    L,x,y=map(int,input().split())
    goods=dict()
    for __ in range(L):
        r,q=input().split()
        q=int(q)
        goods[r]=q
    markets.append((x,y,goods))

def dist(a,b):
    return abs(a[0]-b[0])+abs(a[1]-b[1])

dp=[[-1]*(1<<N) for _ in range(N+1)]
# dp[i][S]: max profit ending at position i(0:market, 1~N:city i-1), visited cities S bitmask 
dp[0][0]=0

pos=[(0,0)]+[(m[0],m[1]) for m in markets]

# Precompute profit for each subset of cities and the best set of items buyable within W
from itertools import combinations,product

# For each city, compute profit per item: buy_price - market_price
profit_per_city=[dict() for _ in range(N)]
for i,(x,y,goods) in enumerate(markets):
    for s,v_p in items.items():
        if s in goods:
            buy_p=goods[s]
            sell_p=v_p[1]
            prof=sell_p - buy_p
            if prof>0:
                profit_per_city[i][s]=prof
        # else no profit; ignore

# For each subset of cities, compute:
# total_profit and minimal weight packing of items (knapsack)
# As unlimited items, do unbounded knapsack over union of items in those cities

# To accelerate, for each city subset:
# collect all items available, with their weight (v), profit (sum of city profits)
# Because multiple cities may sell same item at different prices, pick best profit per item among those cities

def best_profit_for_subset(city_subset):
    # city_subset: tuple of city indices
    goods=dict()
    for c in city_subset:
        for s,p in profit_per_city[c].items():
            if s not in goods or goods[s]<p:
                goods[s]=p
    if not goods:
        return 0
    # dp knapsack: max profit with weight limit W, unlimited items
    dp_knap=[0]*(W+1)
    for s,p in goods.items():
        w=items[s][0]
        for weight in range(w,W+1):
            val=dp_knap[weight-w]+p
            if val>dp_knap[weight]:
                dp_knap[weight]=val
    return max(dp_knap)

from itertools import combinations
subset_profit=dict()
# generate all subsets of cities (non-empty)
for l in range(1,N+1):
    for comb in combinations(range(N),l):
        subset_profit[comb]=best_profit_for_subset(comb)

# Precompute travel time between nodes
dist_map=[[0]*(N+1) for _ in range(N+1)]
for i in range(N+1):
    for j in range(N+1):
        dist_map[i][j]=dist(pos[i],pos[j])

from itertools import chain
for visited in range(1<<N):
    for last in range(N+1):
        if dp[last][visited]<0:
            continue
        # Try to add a subset of unvisited cities and go back to market
        unvisited=[i for i in range(N) if not (visited>>i)&1]
        # Enumerate subsets of unvisited cities
        # To speed up, enumerate subsets by bitmask of unvisited only
        if not unvisited:
            continue
        u_len=len(unvisited)
        for submask in range(1,1<<u_len):
            subset=[]
            for idx in range(u_len):
                if (submask>>idx)&1:
                    subset.append(unvisited[idx])
            # time cost:
            # from pos[last] to first city in subset, go through subset in any order? To minimize time, we can consider:
            # Since we always must go market->cities->market for each purchase set, we consider trip as:
            # from current last to cities subset in any order, then back to market(0)
            # We'll approximate as:
            # The shortest route visiting all cities in subset starting at pos[last], ending at market(0)
            # N is small; do tsp for subset + start,last
            # But number of subsets and tsp is heavy, so we approximate:
            # time = dist(last,cities1)+sum dist between cities in any order + dist(last city,market)
            # But complicated; better to fix order: so we treat subset as one "trip": market -> set of cities -> market
            # So must go from market(0) to each city and back. Since trade happens by going market->cities->market cycles.
            # So from last to market, + from market to cities + from cities to market
            # So cost = dist(last,0) + TSP(market->subset cities->market)
            # Let's approximate by sum of distances to/from market:
            # The minimal route visiting all cities from market and returning market is at least:
            # minimal spanning: 2*sum dist between market and those cities in worst case (go and return city by city)
            # To estimate tight travel time, we calculate TSP starting and ending at market(0)

            # To keep it simple and acceptable:
            # Approximate travel time = dist(last,0) + 2 * sum of dist between market(0) and cities
            # Actually find min of: TSP starting/ending at 0 over subset
            subset_points=[0]+[i+1 for i in subset]
            tsp_dp=[ [float('inf')]*(len(subset_points)) for _ in range(1<<len(subset_points))]
            tsp_dp[1][0]=0
            for s in range(1<<len(subset_points)):
                for u in range(len(subset_points)):
                    if tsp_dp[s][u]==float('inf'):
                        continue
                    for v in range(1,len(subset_points)):
                        if (s>>v)&1==0:
                            cost=dist_map[subset_points[u]][subset_points[v]]
                            ns=s|(1<<v)
                            if tsp_dp[ns][v]>tsp_dp[s][u]+cost:
                                tsp_dp[ns][v]=tsp_dp[s][u]+cost
            full=(1<<len(subset_points))-1
            min_tsp=float('inf')
            for u in range(1,len(subset_points)):
                cost=tsp_dp[full][u]+dist_map[subset_points[u]][0]
                if cost<min_tsp:
                    min_tsp=cost
            travel_time=dist_map[last][0]+min_tsp
            if travel_time>T:
                continue
            p=dp[last][visited]+subset_profit[tuple(sorted(subset))]
            if dp[0][visited|sum(1<<x for x in subset)]<p:
                dp[0][visited|sum(1<<x for x in subset)]=p

ans=max(dp[0])
print(ans if ans>=0 else 0)