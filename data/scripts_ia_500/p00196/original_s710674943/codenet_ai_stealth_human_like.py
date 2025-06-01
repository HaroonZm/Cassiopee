# AOJ 0196 Baseball Championship
# Python3 solution with some personal tweaks and comments
# 2018.6.21 bal4u

while True:
    n = int(input())
    if n == 0:
        break  # End of input
    
    teams = []
    for idx in range(n):
        parts = input().split()
        team_name = parts[0]
        results = parts[1:]
        
        wins = 0
        losses = 0
        
        for res in results:
            val = int(res)
            if val == 0:
                wins += 1   # win count increment
            elif val == 1:
                losses += 1  # loss count increment
            # I'm ignoring any other values just in case
        
        # Store as tuple with index to keep original order as tiebreaker
        teams.append((team_name, idx, wins, losses))
    
    # Sort by wins descending, then losses ascending, then original order
    sorted_teams = sorted(teams, key=lambda x: (-x[2], x[3], x[1]))
    
    for team in sorted_teams:
        print(team[0])  # print the team name only, no extras