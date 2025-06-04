import sys
import bisect

def main():
    input = sys.stdin.readline
    N, L = map(int, input().split())
    intervals = [tuple(map(int, input().split())) for _ in range(N)]

    # ------- Part 1: Compute x -------
    # x = minimum number of intervals to cover [0, L)

    # Approach:
    # Use a greedy algorithm to cover [0, L):
    # 1. Sort intervals by their start point.
    # 2. From the current coverage end (start=0 initially), 
    #    find the interval(s) with l_i <= current coverage_end 
    #    that extends coverage_end the most (maximum r_i).
    # 3. Select that interval, update coverage_end to the furthest r_i found.
    # 4. Repeat until coverage_end >= L or no suitable interval found.

    intervals.sort(key=lambda x: (x[0], -x[1]))

    count = 0
    coverage_end = 0
    idx = 0
    furthest = 0

    while coverage_end < L:
        # Find intervals starting at or before coverage_end
        # that extends coverage_end the furthest.
        while idx < N and intervals[idx][0] <= coverage_end:
            if intervals[idx][1] > furthest:
                furthest = intervals[idx][1]
            idx += 1

        if furthest == coverage_end:
            # No progress possible, coverage incomplete (should not happen due to problem assumption)
            # but we handle it safely.
            break

        coverage_end = furthest
        count += 1

    x = count  # minimum number of intervals to cover [0,L)

    # ------- Part 2: Compute y -------
    # y = minimum integer such that any y intervals from given intervals cover [0,L)
    #
    # Equivalently: y = N - m + 1 where m is the size of the largest subset of intervals whose union does NOT cover [0,L)
    #
    # So we find the maximum number m of intervals which fail to cover [0,L). Then y = N - m + 1.
    #
    # Approach to find m:
    # We try to find a large combination of intervals that miss some part of [0,L).
    #
    # Using greedy for coverage again:
    # The maximal subset that does NOT cover [0,L) is largest when it cannot cover at least one subinterval in [0,L).
    #
    # To find such set, we use the greedy approach:
    # - Sort intervals by their start again.
    # - Try to cover from 0 to L using selected intervals.
    #   The intervals selected are minimum to cover [0,L), so the intervals NOT selected can fail to cover.
    #
    # But we want the maximal subset that DOES NOT cover [0,L).
    #
    # Instead, more directly:
    # - For each interval, check if it is part of some minimal cover set or essential for coverage.
    # - If we can find minimal covers of size x, then removing any y = N - x + 1 intervals
    #   would guarantee coverage.
    #
    # However, this is tricky.
    #
    # According to the problem, the minimal number to guarantee coverage for ANY choice of that many intervals is:
    # y = minimum integer such that ALL combinations of y intervals cover [0,L).
    #
    # That means any subset with size < y does NOT necessarily cover [0,L).
    # So y = N - max number of intervals in a subset that fails to cover + 1.
    #
    # To find m = max subset that does NOT cover:
    # - If we remove some intervals, check if the rest cover or not.
    #
    # Since N can be large, we must do this efficiently.
    #
    # Key property from the problem and constraints:
    # Because the union of all intervals is [0,L), we can think in terms of interval endpoints:
    #
    # Let's analyze by intervals sorted by l_i:
    # We will find all pairs of intervals that form a gap when combined with the rest. But better:
    #
    # The minimal set that covers is of size x (already computed).
    #
    # The maximal subset that does NOT cover can be found by removing from the set the minimal cover,
    # so m = N - x.
    #
    # But the example shows y can be > x.
    #
    # Another approach based on the editorial logic:
    #
    # Consider all intervals, try to find the minimal number of intervals whose set of complements covers [0,L).
    # So y = minimal number such that any subset of size y covers, meaning: subsets of size N - y fail to cover at most.
    #
    # Thus, find the maximal subset size with no coverage:
    # We can use the greedy approach reversed:
    #
    # Create intervals sorted by their start, iterate by start then by end:
    # For maximal non-cover subset:
    #   - Starting from 0, try to cover as far as possible using intervals
    #   - At each point, add intervals that extend coverage
    #   - Track intervals that do not contribute to coverage, we can add as many as possible into non-cover sets.
    #
    # But the problem constraints large, so let's rely on an interval coverage greedy approach with interval removal checks.
    #
    # Algorithm:
    # Compute the minimal coverage set (x intervals) using Part 1.
    # Now consider intervals not in that minimal set, add them to a non-cover subset.
    #
    # Could we have a bigger non-cover subset by leaving out intervals from the minimal set?
    #
    # What about intervals covering the critical junctions?
    #
    # Actually, to find m:
    # Use a "set coverage check" trick:
    #
    # 1. Sort intervals by their start.
    # 2. For each interval, represent it by (l_i, r_i).
    #
    # We want the maximum subset with union NOT equal [0,L):
    # - Such subset misses some point in [0,L).
    #
    # Because the union of all intervals is [0,L), the only missing points are covered by required intervals.
    #
    # So the largest subset missing coverage is largest subset excluding at least one minimal cover interval.
    #
    # Because minimal cover requires x intervals, any subset lacking at least one of those x intervals possibly misses coverage.
    # So largest non-covering subset size = N - x.
    #
    # BUT check the sample test case where y > x.
    #
    # So minimal cover is not sufficient to determine y.
    #
    # Let's do a "critical point" coverage analysis:
    #
    # For each position from 0 to L, find how many intervals cover it.
    #
    # The minimal coverage at any point is the minimal number of intervals covering that point.
    #
    # The minimal minimal coverage over all points is the minimal "coverage redundancy".
    #
    # y = minimal minimal coverage + 1
    #
    # Explanation:
    # If there is a point covered by only k intervals, then if you pick any y = k intervals, 
    # if y <= k, might still miss that point.
    #
    # So to guarantee any y intervals cover, y must be greater than the minimal coverage at any point.
    #
    # So, we find the minimal coverage count among all points in [0,L).
    #
    # Because intervals are half-open [l_i, r_i), coverage changes only at interval endpoints.
    #
    # Approach to find minimal coverage:
    # - Sweep line algorithm:
    #   * Create events at l_i (cover +1) and r_i (cover -1)
    #   * Sort events
    #   * Track current coverage and update minimal coverage
    #
    # The answer y = minimal coverage over all points + 1

    events = []
    for l, r in intervals:
        events.append((l, +1))
        events.append((r, -1))
    events.sort()

    current_coverage = 0
    min_coverage = float('inf')

    # Sweep line to find coverage at every point where coverage changes, 
    # minimal coverage (number of intervals covering any point in [0,L))
    prev_x = 0
    for x, typ in events:
        if x != prev_x:
            if prev_x < x:
                # The coverage between prev_x and x is current_coverage
                # We consider coverage in [prev_x, x) which are points covered by current_coverage intervals
                if current_coverage < min_coverage:
                    min_coverage = current_coverage
            prev_x = x
        current_coverage += typ

    # After processing all events, minimal coverage is min_coverage
    # y = minimal coverage + 1

    # Note: min_coverage >=1 because union covers [0,L), so at least one interval covers each point.

    y = min_coverage + 1

    print(x, y)

if __name__ == "__main__":
    main()