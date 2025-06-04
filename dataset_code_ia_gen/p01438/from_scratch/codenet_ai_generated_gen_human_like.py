import sys

def conflict(dates):
    dates = sorted(dates)
    for i in range(len(dates) - 1):
        if dates[i][1] > dates[i + 1][0]:
            return True
    return False

def main():
    input = sys.stdin.readline
    while True:
        N = int(input())
        if N == 0:
            break
        guys = []
        for _ in range(N):
            M, L = map(int, input().split())
            dates = [tuple(map(int, input().split())) for __ in range(M)]
            # Check if this guy's own dates conflict
            if conflict(dates):
                # Can't keep this guy
                guys.append(([], 0))
            else:
                guys.append((dates, L))
        # We want to choose subset of guys with no overlapping dates
        # N <= 100 -> We can try all subsets with pruning
        max_satisfaction = 0
        # Preprocess guys to their time intervals and satisfaction
        intervals = [guy[0] for guy in guys]
        satisfactions = [guy[1] for guy in guys]
        from itertools import combinations
        # Since N=100 max subsets is too big
        # Use DP with bitmasks? 2^100 too big.
        # Instead implement backtracking with pruning.
        # Sort guys by satisfaction descending to try big first
        order = sorted(range(N), key=lambda x: satisfactions[x], reverse=True)
        selected_intervals = []
        selected_times = []
        def can_add(new_dates):
            # Check no overlap with current selected_times
            # dates are intervals [start,end)
            for ns, ne in new_dates:
                for ss, se in selected_times:
                    if not (ne <= ss or ns >= se):
                        return False
            return True
        def dfs(i, current_sum):
            nonlocal max_satisfaction
            if i == N:
                if current_sum > max_satisfaction:
                    max_satisfaction = current_sum
                return
            # Prune if even taking all next satisfactions can't beat max
            rem = 0
            for j in range(i, N):
                rem += satisfactions[order[j]]
            if current_sum + rem <= max_satisfaction:
                return
            idx = order[i]
            # Option1: skip guy idx
            dfs(i+1, current_sum)
            # Option2: try to add guy idx if no conflicts
            if satisfactions[idx] > 0 and can_add(intervals[idx]):
                selected_times.extend(intervals[idx])
                dfs(i+1, current_sum + satisfactions[idx])
                # backtrack
                del selected_times[-len(intervals[idx]):]
        dfs(0, 0)
        print(max_satisfaction)

if __name__ == "__main__":
    main()