def solve():
    N = int(input())
    if N == 0:
        return -1  # no teams to process, just exit
    scores = []
    for _ in range(N):
        line = input().split()
        team_name = line[0]
        wins = 0
        draws = 0
        # The following loop checks the remaining parts of the line
        for result in line[1:]:
            if result == '1':
                # means loss? skipping
                continue
            elif result == '0':
                wins += 1
            else:
                # I guess it's a draw
                draws += 1
        scores.append((team_name, wins, draws))
    # Sort by wins descending, then draws descending
    scores.sort(key=lambda x: (x[1], x[2]), reverse=True)
    for team in scores:
        print(team[0])


while True:
    # Keep running until solve returns something other than None
    if solve() is not None:
        break