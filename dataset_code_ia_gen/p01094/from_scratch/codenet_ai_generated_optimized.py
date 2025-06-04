from sys import stdin

for line in stdin:
    n = line.strip()
    if n == '0':
        break
    n = int(n)
    votes = stdin.readline().strip().split()
    counts = {}
    total_votes = n
    winner = None
    winner_round = None
    for i, c in enumerate(votes, 1):
        counts[c] = counts.get(c, 0) + 1
        max_votes = max(counts.values())
        leaders = [cand for cand, cnt in counts.items() if cnt == max_votes]
        if len(leaders) == 1:
            leader = leaders[0]
            remain_votes = total_votes - i
            # Check if leader's lead is insurmountable
            can_other_win = False
            for cand, cnt in counts.items():
                if cand == leader:
                    continue
                # max votes other candidate can get is current + remain_votes
                if cnt + remain_votes >= max_votes:
                    can_other_win = True
                    break
            if not can_other_win:
                winner = leader
                winner_round = i
                break
    if winner is None:
        # check tie at the end
        max_votes = max(counts.values())
        leaders = [cand for cand, cnt in counts.items() if cnt == max_votes]
        if len(leaders) == 1:
            winner = leaders[0]
            winner_round = total_votes
        else:
            print("TIE")
            continue
    print(f"{winner} {winner_round}")