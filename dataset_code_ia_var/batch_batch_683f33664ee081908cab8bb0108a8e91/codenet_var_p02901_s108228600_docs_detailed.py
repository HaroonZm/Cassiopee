def min_cost_to_unlock_all_boxes():
    """
    Reads the number of boxes and keys, then reads the list of keys (each with coverage and cost).
    Computes the minimum cost to open all boxes using dynamic programming over bitmasks.
    Prints the minimal total cost or -1 if not all boxes can be opened.
    """
    # Read the number of boxes N, and the number of keys M
    N, M = map(int, input().split())

    # List to hold each key as a tuple: (bitmask of boxes it can open, cost)
    keys = []
    for _ in range(M):
        # Read the cost 'a' and the number of boxes this key can open 'b'
        a, b = map(int, input().split())
        # Read list 'c' of which boxes (1-indexed) this key can open
        c = list(map(int, input().split()))
        s = 0  # Bitmask representing boxes this key can open (0 means box closed)
        for cc in c:
            cc -= 1         # Convert to 0-based indexing
            s |= 1 << cc    # Set the bit corresponding to box cc
        # Append this key's bitmask and cost
        keys.append((s, a))

    # Dynamic Programming table:
    # dp[state] = minimal cost required to reach 'state' (which boxes opened)
    dp = [float('inf')] * (1 << N)
    # Base case: cost to open no boxes is 0
    dp[0] = 0

    # Loop over all possible states (sets of opened boxes)
    for s in range(1 << N):
        for i in range(M):
            # t: state if using key i from current state s
            t = s | keys[i][0]  # Open any boxes attainable by this key
            # Update the minimal cost to reach state t
            dp[t] = min(dp[t], keys[i][1] + dp[s])

    # If it's impossible to open all boxes (dp[-1] is infinite), output -1
    if dp[-1] == float('inf'):
        print(-1)
    else:
        # Else, print minimal cost to open all boxes
        print(dp[-1])