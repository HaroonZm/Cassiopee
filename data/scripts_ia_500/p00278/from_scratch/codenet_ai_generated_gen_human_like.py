import sys
import bisect

input = sys.stdin.readline

N, Q = map(int, input().split())
scores = [int(input()) for _ in range(N)]

leaders = {}
leader_scores = []

def impossible(low, high, x):
    # binary search for minimal r
    # check if there are > x students that cannot join any group at distance <= mid
    while low < high:
        mid = (low + high) // 2
        cannot_join = 0

        # For every student, check if it can join a leader's group with r=mid
        # condition: leader_score s <= student_score < s + r + 1
        # or student_score >= s and student_score < s + r + 1
        # but only those groups with leader_score <= student_score possible
        # Here reverse logic: for student score si
        # find leader s where s <= si and si < s + r + 1 == s + r + 1 > si >= s
        # So for fixed r, group intervals: [s, s+r]
        # student can't join any if there is no leader s with s <= si <= s + r

        # Sort leaders:
        ls = leader_scores
        if not ls:
            # no leader => all cannot join
            cannot_join = N
            if cannot_join <= x:
                high = mid
            else:
                low = mid + 1
            continue

        # We'll use bisect to speed up for each student
        # Since leaders <= 100, iterate for every student may be too slow (N up to 1e6)
        # So we optimize:
        # We consider intervals: for each leader s: [s, s+r]
        # The union of intervals covers the allowed student scores.
        # We can merge intervals and count how many students fall outside.

        # Build intervals and merge them
        intervals = []
        for s in ls:
            intervals.append((s, s + mid))
        intervals.sort()

        merged = []
        cur_start, cur_end = intervals[0]
        for st, en in intervals[1:]:
            if st <= cur_end + 1:
                cur_end = max(cur_end, en)
            else:
                merged.append((cur_start, cur_end))
                cur_start, cur_end = st, en
        merged.append((cur_start, cur_end))

        # Count how many scores are outside merged intervals
        # scores are known, also sort scores ascending with indices
        # scores sorted ascending with their positions
        # Since scores input order is fixed, pre-sort here for speed
        # We can pre-sort once outside ?

        # Let's pre-sort scores once
        # To prevent recomputing every binary search, we do it outside impossible

        cannot_join = 0
        idx = 0
        for st, en in merged:
            # Count how many scores < st
            # scores are sorted ascending
            while idx < N and scores_sorted[idx] < st:
                cannot_join += 1
                idx += 1
            # advance idx past scores in [st,en]
            while idx < N and st <= scores_sorted[idx] <= en:
                idx += 1
        # Remaining scores after last interval are outside
        cannot_join += N - idx

        if cannot_join <= x:
            high = mid
        else:
            low = mid + 1

    return low

# Pre-sort once
scores_sorted = sorted(scores)

for _ in range(Q):
    line = input().split()
    cmd = line[0]
    if cmd == "ADD":
        a = int(line[1]) - 1
        s = scores[a]
        if a not in leaders:
            leaders[a] = s
            bisect.insort(leader_scores, s)
    elif cmd == "REMOVE":
        a = int(line[1]) - 1
        if a in leaders:
            s = leaders[a]
            idx = bisect.bisect_left(leader_scores, s)
            leader_scores.pop(idx)
            del leaders[a]
    else:
        x = int(line[1])
        if not leader_scores:
            # no leader => all students cannot join
            if x >= N:
                print(0)
            else:
                print("NA")
            continue
        low = 0
        high = 10**10  # large enough upper bound
        res = impossible(low, high, x)
        # check if res actually valid
        # verify with cannot_join at res, if cannot_join <= x
        # if cannot_join > x => NA
        mid = res
        ls = leader_scores

        intervals = []
        for s in ls:
            intervals.append((s, s + mid))
        intervals.sort()

        merged = []
        cur_start, cur_end = intervals[0]
        for st, en in intervals[1:]:
            if st <= cur_end + 1:
                cur_end = max(cur_end, en)
            else:
                merged.append((cur_start, cur_end))
                cur_start, cur_end = st, en
        merged.append((cur_start, cur_end))

        cannot_join = 0
        idx = 0
        for st, en in merged:
            while idx < N and scores_sorted[idx] < st:
                cannot_join += 1
                idx += 1
            while idx < N and st <= scores_sorted[idx] <= en:
                idx += 1
        cannot_join += N - idx

        if cannot_join <= x:
            print(res)
        else:
            print("NA")