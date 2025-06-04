def can_learn_all_commands():
    import sys
    input = sys.stdin.readline

    M, N = map(int, input().split())
    # Initialize skill bounds
    # low[i] = minimum skill points for skill i (initialized to 0)
    # high[i] = maximum skill points for skill i (initialized to something large)
    low = [0]*N
    high = [100]*N

    for _ in range(M):
        K = int(input())
        for __ in range(K):
            s, cond, t = input().split()
            s = int(s)-1
            t = int(t)
            if cond == ">=":
                # skill s needs to be >= t
                # update low bound
                if low[s] < t:
                    low[s] = t
            else:
                # cond == "<="
                # skill s <= t
                # update high bound
                if high[s] > t:
                    high[s] = t

    # Check if for all skills low[i] <= high[i]
    for i in range(N):
        if low[i] > high[i]:
            print("No")
            return
    print("Yes")

can_learn_all_commands()