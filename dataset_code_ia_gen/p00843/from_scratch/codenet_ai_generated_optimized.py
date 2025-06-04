import sys
input = sys.stdin.readline

def all_lines(m):
    lines = []
    for i in range(m):
        lines.append([(i,j) for j in range(m)])   # row i
        lines.append([(j,i) for j in range(m)])   # column i
    lines.append([(i,i) for i in range(m)])       # main diagonal
    lines.append([(i,m-1-i) for i in range(m)])   # anti diagonal
    return lines

def solve():
    while True:
        P,M = map(int,input().split())
        if P==0 and M==0:
            break
        cards = []
        for _ in range(P):
            row = list(map(int,input().split()))
            card = [row[i*M:(i+1)*M] for i in range(M)]
            cards.append(card)
        # For each card, for each line, store the numbers forming that line
        lines = all_lines(M)
        card_lines = []
        for c in range(P):
            clines = []
            for ln in lines:
                clines.append(set(cards[c][i][j] for i,j in ln))
            card_lines.append(clines)

        # For each card, find minimal numbers needed for a line to bingo
        # But we want to order the bingo finishing times:
        # The gamemaster can choose order of calling numbers, to satisfy condition that card_i bingo no later than card_j if i<j.
        # We seek minimal length of sequence of numbers satisfying the condition.
        #
        # Modeling:
        # Each card can bingo on any line.
        # The bingo time of the card = max of called numbers in chosen line (numbers called so far).
        # The gamemaster controls call order so to order bingo times by card index ascending.
        #
        # We'll try to find, for each card, a line and assign finishing times (the max called number in that line),
        # such that finishing times are nondecreasing in card order,
        # and total unique numbers used in all chosen lines is minimal.
        #
        # To model that, build all combinations candidate finishing times by choosing one line per card.
        #
        # But possibly huge.
        # Because P<=4, M<=4, total lines are max 2*M+2=10.
        #
        # We'll proceed with a branch and bound search:
        # For each card, try all lines.
        # Determine finish_time (max number in line) for that card.
        # Enforce finish_time[i] <= finish_time[i+1]
        #
        # To minimize total unique numbers selected, accumulate the union of sets.
        #
        # We'll implement DFS with pruning.

        from functools import lru_cache

        cards_lines_sets = card_lines
        P_lines = [len(card_lines[i]) for i in range(P)]  # number of lines per card

        # Precompute for each card and line:
        # line_set: set of numbers in line
        # max_num_line: max number in line
        line_info = []
        for c in range(P):
            info = []
            for s in cards_lines_sets[c]:
                mx = max(s)
                info.append((s,mx))
            line_info.append(info)

        min_length = float('inf')

        # Order lines for efficiency: sort by max number ascending (to get smaller finishing times first)
        for c in range(P):
            line_info[c].sort(key=lambda x:x[1])

        # DFS:
        # idx: current card index
        # last_finish_time: finish_time of previous card
        # used_numbers:set of numbers used so far
        def dfs(idx,last_finish_time,used_numbers):
            nonlocal min_length
            if idx==P:
                min_length = min(min_length,len(used_numbers))
                return
            # bound: if used numbers already >= min_length, prune
            if len(used_numbers)>=min_length:
                return
            for s,mx in line_info[idx]:
                # enforce condition: finish_time of current line >= last_finish_time
                if mx>=last_finish_time:
                    new_used = used_numbers | s
                    if len(new_used)>=min_length:
                        continue
                    dfs(idx+1,mx,new_used)

        dfs(0,0,set())
        print(min_length if min_length!=float('inf') else 0)

if __name__=="__main__":
    solve()