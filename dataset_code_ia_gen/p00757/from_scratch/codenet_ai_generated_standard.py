import sys
sys.setrecursionlimit(10**7)

def main():
    input = sys.stdin.readline

    while True:
        h,w,s = map(int,input().split())
        if h==0 and w==0 and s==0:
            break
        U = [list(map(int,input().split())) for _ in range(h)]

        # prefix sum
        P = [[0]*(w+1) for _ in range(h+1)]
        for y in range(1,h+1):
            for x in range(1,w+1):
                P[y][x] = U[y-1][x-1] + P[y-1][x] + P[y][x-1] - P[y-1][x-1]

        def demand(y0,x0,y1,x1):
            return P[y1][x1] - P[y0][x1] - P[y1][x0] + P[y0][x0]

        from functools import lru_cache

        @lru_cache(None)
        def dp(y0,x0,y1,x1):
            total = demand(y0,x0,y1,x1)
            if total <= s:
                return (1,s - total)
            best = (1, s - total)  # fallback no cut
            # horizontal cuts
            for y in range(y0+1,y1):
                top = dp(y0,x0,y,x1)
                bot = dp(y,x0,y1,x1)
                groups = top[0] + bot[0]
                # max suppressed demand = max among all but one groups
                # max suppressed demand = max of sum of demands of all groups minus minimal group demand
                # The reserve power = s - (max suppressed demand)
                # max suppressed demand = max(total demand of all groups except one)
                # = max(total sum - minimal group demand)
                # groups reserve depends on minimal group demand, which >= 0
                # But since dp gives (groups, reserve), reserve = s - max_suppressed_demand
                # We need to select max(groups) then max(reserve)
                min_group_demand = total - (s - top[1]) if top[1]>=0 else float('inf')
                min_group_demand = min(min_group_demand, total - (s - bot[1]) if bot[1]>=0 else float('inf'))
                # Actually better to calculate max suppressed demand = max total demand of all but one group = total - min group demand
                # s - (total - min_group_demand) = reserve power
                max_supp = total - min(top[1]+top[1],bot[1]+bot[1])
                # Instead, just use the formula: reserve = min(top_rec[1], bot_rec[1]) (as in dp)
                # To avoid confusion we use dp value directly as per original, just compare groups and reserve:
                # check better groups
                cand_reserve = min(top[1], bot[1])  # minimal reserve of subareas
                cand_groups = groups
                if cand_groups > best[0] or (cand_groups == best[0] and cand_reserve > best[1]):
                    best = (cand_groups,cand_reserve)

                # Correct way is just consider best among dp returns
                # So more correct is:
                # combine top and bot: groups=top+bot
                # the max suppressed demand = max of all-but-one groups among all groups.
                # Because the set of groups is union of subgroups of top and bot,
                # max suppressed demand is max of total sum - min demand group among all groups.
                # That means reserve = min over groups minimal group demand
                # The dp returns reserve=s - max_suppressed_demand
                # So reserve of grouping is minimum of reserve of top and bot.

                # So finally:
                # Reserve = min(top reserve, bot reserve)
                # Number of groups = sum of groups
                # Compare to best by groups then reserve.
            # vertical cuts
            for x in range(x0+1,x1):
                left = dp(y0,x0,y1,x)
                right = dp(y0,x,y1,x1)
                groups = left[0]+right[0]
                cand_reserve = min(left[1], right[1])
                cand_groups = groups
                if cand_groups > best[0] or (cand_groups == best[0] and cand_reserve > best[1]):
                    best = (cand_groups,cand_reserve)
            return best

        res = dp(0,0,h,w)
        print(res[0],res[1])

if __name__ == '__main__':
    main()