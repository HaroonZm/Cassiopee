while True:
    n, U = map(int, input().split())
    if n == 0 and U == 0:
        break
    credits = [0]*n
    prereqs = [[] for _ in range(n)]
    for i in range(n):
        parts = list(map(int, input().split()))
        c = parts[0]
        k = parts[1]
        r = parts[2:] if k > 0 else []
        credits[i] = c
        prereqs[i] = r

    ans = n+1
    # bruteforce all combinations
    # for each subset, check if all prereqs for included courses are in the subset
    # if sum credits >= U, update ans with minimal size
    from itertools import combinations

    for size in range(1, n+1):
        combs = combinations(range(n), size)
        for comb in combs:
            selected = set(comb)
            # check prereqs condition
            ok = True
            for course in comb:
                for pre in prereqs[course]:
                    if pre not in selected:
                        ok = False
                        break
                if not ok:
                    break
            if not ok:
                continue
            total_credits = sum(credits[c] for c in selected)
            if total_credits >= U:
                ans = size
                break
        if ans != n+1:
            break

    print(ans)