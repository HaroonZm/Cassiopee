import sys
import bisect

input = sys.stdin.readline

N, Q = map(int, input().split())
scores = [int(input()) for _ in range(N)]

leaders_set = set()
leaders_scores = []

def update_leaders_scores():
    global leaders_scores
    leaders_scores = sorted(scores[i-1] for i in leaders_set)

def count_unreachable(r):
    if not leaders_scores:
        return N
    count = 0
    L = leaders_scores
    for sc in scores:
        # Find leader with score <= sc and leader_score >= sc - r
        # Condition: leader_score <= sc and leader_score >= sc - r
        # So leader_score in [sc - r, sc]
        left = sc - r
        right = sc
        # Find left boundary
        li = bisect.bisect_left(L, left)
        # Find right boundary
        ri = bisect.bisect_right(L, right)
        if li == ri:
            count += 1
    return count

for _ in range(Q):
    query = input().split()
    if query[0] == "ADD":
        a = int(query[1])
        leaders_set.add(a)
        # update leaders_scores
        # Since max leaders 100, just sort every time
        update_leaders_scores()
    elif query[0] == "REMOVE":
        a = int(query[1])
        leaders_set.remove(a)
        update_leaders_scores()
    else:  # CHECK x
        x = int(query[1])
        if not leaders_scores:
            # No leaders, unreachable = N
            print("0" if x >= N else "NA")
            continue
        # Binary search on r: 0 to max_possible
        # max_possible = max score - min score
        left = 0
        right = 10**9
        ans = None
        while left <= right:
            mid = (left + right) // 2
            unreachable = count_unreachable(mid)
            if unreachable <= x:
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        if ans is None:
            print("NA")
        else:
            print(ans)