def read_number_of_teams():
    return int(input())

def should_stop(n):
    return n == 0

def read_team_line():
    return input().split()

def extract_team_name_and_results(line):
    team_name = line.pop(0)
    results = line
    return team_name, results

def count_wins_and_losses(results):
    wins = 0
    losses = 0
    for result in results:
        if int(result) == 0:
            wins += 1
        elif int(result) == 1:
            losses += 1
    return wins, losses

def create_team_record(team_name, index, wins, losses):
    return (team_name, index, wins, losses)

def read_all_teams(n):
    teams = []
    for i in range(n):
        line = read_team_line()
        team_name, results = extract_team_name_and_results(line)
        wins, losses = count_wins_and_losses(results)
        team_record = create_team_record(team_name, i, wins, losses)
        teams.append(team_record)
    return teams

def sort_teams(teams):
    return sorted(teams, key=lambda x: (-x[2], x[3], x[1]))

def print_team_name(team_record):
    print(team_record[0])

def main_loop():
    while True:
        n = read_number_of_teams()
        if should_stop(n):
            break
        teams = read_all_teams(n)
        sorted_teams = sort_teams(teams)
        for team in sorted_teams:
            print_team_name(team)

main_loop()