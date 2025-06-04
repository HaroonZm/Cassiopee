while True:
    n = input()
    if n == '0':
        break
    n = int(n)
    votes = input().split()
    counts = {}
    for c in votes:
        counts[c] = 0
    total_votes = n
    winner = None
    winner_at = None
    for i, v in enumerate(votes, 1):
        counts[v] += 1
        max_votes = max(counts.values())
        leaders = [k for k, val in counts.items() if val == max_votes]
        if len(leaders) == 1:
            leader = leaders[0]
            remaining = total_votes - i
            # Check if leader's lead is insurmountable
            can_others_catch = any(max_votes - counts[cand] <= remaining for cand in counts if cand != leader)
            if not can_others_catch:
                winner = leader
                winner_at = i
                break
    if winner is None:
        # check if tie or single winner at the end
        max_votes = max(counts.values())
        leaders = [k for k, val in counts.items() if val == max_votes]
        if len(leaders) == 1:
            winner = leaders[0]
            winner_at = n
        else:
            print("TIE")
            continue
    print(f"{winner} {winner_at}")