def main():
    import sys
    sys.setrecursionlimit(10**7)
    input_lines = sys.stdin.read().splitlines()
    pos = 0
    while True:
        if pos >= len(input_lines):
            break
        line = input_lines[pos].strip()
        pos += 1
        if line == '':
            continue
        C,D,W,X = map(int,line.split())
        if C==0 and D==0 and W==0 and X==0:
            break
        E = []
        for i in range(C):
            row = list(map(int,input_lines[pos].split()))
            pos += 1
            E.append(row)
        F = []
        for i in range(C):
            row = list(map(int,input_lines[pos].split()))
            pos += 1
            F.append(row)

        # For each day j from 0 to D-1, we precompute all subsets of regions with E[i][j]>0 (regions where live can be held)
        # The conditions:
        # - On day j, can perform one or more lives following adjacency rule and no repeating same region same day
        # - adjacency is linear: region i connected to i-1 and i+1 only (except edges)
        # - For subset of regions selected in day j performance, the regions must be connected intervals in i (since adjacency is linear)
        #   or can moves start in one region and move to neighbors, but multiple intervals are not connected
        # But statement says "ある地域でライブを行った後、隣接する地域でライブを行える場合はその地域で同じ日に再びライブを行うことができる。"
        # That means that multiple live performances in same day can be done if they form connected sequence (linear chain)
        # So the set of regions selected on a day must be a connected chain of regions with E[i][j]>0 and no region repeated.
        # So for day j, possible performances are intervals of regions i1 to i2 with E[i][j]>0, and the chain goes from i1 to i2 or reverse, but since the chain is linear adjacency, the set must be continuous in index.
        # So possible multi-live sets on a day are contiguous intervals of regions where all E[i][j]>0.
        # Single region is also allowed.

        # So for each day j, find all intervals i1<=i<=i2 with i from 0 to C-1, where all E[i][j]>0.
        # For each such interval, compute sum of E and sum of F for that day.
        # Since same day multi-live day count (count of days with multiple lives) <= X.
        # Total burden sum <= W.

        # We'll do DP on days:
        # State: day, burden_used, multi_live_day_count
        # For burden_used from 0 to W
        # For multi_live_day_count from 0 to X
        # DP stores max profit

        # Since W=50 max, X=5 max, D=30, C=15, we can do it.

        # For each day, prepare all possible performances:
        # For one live in region i (if E[i][j]>0)
        # For intervals i1<=i2 of length >=1 where all E[i][j]>0

        # To simplify:
        # For day j:
        # for i1 in 0..C-1:
        #   for i2 in i1..C-1:
        #     if all E[k][j]>0 for k in i1..i2:
        #       sumE, sumF for those regions and day j
        #     else: skip

        max_profit = [[[-1]*(X+1) for _ in range(W+1)] for _ in range(D+1)]
        max_profit[0][0][0] = 0

        for day in range(D):
            # build performances
            performances = []
            for start in range(C):
                # stop if E[start][day]==0 continue to next start
                if E[start][day]==0:
                    continue
                sumE_perf = 0
                sumF_perf = 0
                for end in range(start,C):
                    if E[end][day] == 0:
                        break
                    sumE_perf += E[end][day]
                    sumF_perf += F[end][day]
                    length = end - start + 1
                    # if length ==1 => single live day
                    # if length >1 => multi live day
                    multi = 1 if length>1 else 0
                    performances.append((sumF_perf,speed:=sumE_perf,multi))
            # Also consider no live on this day
            performances.append((0,0,0))

            for w_used in range(W+1):
                for x_used in range(X+1):
                    if max_profit[day][w_used][x_used] == -1:
                        continue
                    current_profit = max_profit[day][w_used][x_used]
                    for burden,profit,multi in performances:
                        nw = w_used + burden
                        nx = x_used + multi
                        if nw <= W and nx <= X:
                            if max_profit[day+1][nw][nx] < current_profit + profit:
                                max_profit[day+1][nw][nx] = current_profit + profit

        ans = 0
        for w_used in range(W+1):
            for x_used in range(X+1):
                if max_profit[D][w_used][x_used] > ans:
                    ans = max_profit[D][w_used][x_used]
        print(ans)

if __name__ == "__main__":
    main()