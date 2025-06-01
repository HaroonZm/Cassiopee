import sys
import operator

file_input = sys.stdin

while True:
    num_teams = int(file_input.readline())
    if num_teams == 0:
        # That's the end of input
        break
    teams_data = [file_input.readline().split() for _ in range(num_teams)]
    
    # Trying to create tuples with team name, neg count of zeros, count of ones, and original index
    processed_teams = []
    for idx, team in enumerate(teams_data):
        name = team[0]
        zeros = team.count('0')  # counting zeros in the list
        ones = team.count('1')
        # Negative zeros to sort ascending properly maybe?
        processed_teams.append((name, -zeros, ones, idx))
    
    # Sort by negative zeros, then ones, then original index
    processed_teams.sort(key=operator.itemgetter(1, 2, 3))
    
    # Print the team names in the new order
    for team in processed_teams:
        print(team[0])