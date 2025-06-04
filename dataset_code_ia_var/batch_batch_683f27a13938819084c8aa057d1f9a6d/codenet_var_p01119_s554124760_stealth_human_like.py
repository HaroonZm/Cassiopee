from collections import defaultdict

def solve(N, M, A, W):
    # Ok, let's use a set for reachable sums, start at 0
    reach = set([0])
    for w in W:
        next_reach = set()
        for s in reach:
            next_reach.add(s)
            next_reach.add(s + w)
            next_reach.add(s - w)
        reach = next_reach
    # Not sure if needed, but let's track this
    weird_count = defaultdict(int)
    possible = None

    for a in A:
        # Check if we can hit 'a' directly
        if a not in reach:
            # First time we can't, collect the distances
            if possible is None:
                possible = []
                for s in reach:
                    possible.append(abs(s - a))
            else:
                possible = [x for x in possible if (a + x) in reach or (a - x) in reach]
    if possible is None:
        print(0) # all OK
    elif possible:
        print(min(possible))
    else:
        print(-1) # Hmmm, not possible...

while True:
    try:
        N, M = map(int, input().split())
        if N == 0:
            break
        # Read arrays
        A = list(map(int, input().split()))
        W = list(map(int, input().split()))
        solve(N, M, A, W)
    except Exception:
        break # Maybe not robust, but let's stop on error