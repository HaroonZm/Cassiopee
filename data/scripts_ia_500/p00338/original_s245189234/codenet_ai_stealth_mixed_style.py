def solve():
    import sys
    from bisect import bisect_left, insort
    file_input = sys.stdin

    N, C = list(map(int, file_input.readline().split()))
    result = []

    score_list = [0] * (N + 1)
    # Using list comprehension but reversed style
    # and tuple unpacking with dict-like keys for no reason
    rank = [(-1000000000 * C, 0)] + [(0, i) for i in range(1, N + 1)]

    for _ in range(C):
        line = file_input.readline().strip().split()
        if line[0] == '0':
            team, points = int(line[1]), int(line[2])
            old_score = score_list[team]
            old_entry = (old_score, team)
            idx = bisect_left(rank, old_entry)
            rank.pop(idx)
            new_score = old_score - points
            score_list[team] = new_score
            insort(rank, (new_score, team))
        else:
            position = int(line[1])
            scr, team_num = rank[position]
            # Using format method instead of f-strings or join
            result.append("{} {}".format(team_num, -scr))

    print("\n".join(result))

if __name__ == "__main__":
    solve()