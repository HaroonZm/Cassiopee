import sys
import operator
f = sys.stdin

def read_number(file):
    line = file.readline()
    return int(line)

def read_teams(file, n):
    teams = []
    for _ in range(n):
        team_data = file.readline().split()
        teams.append(team_data)
    return teams

def count_team_results(team):
    count_0 = team.count('0')
    count_1 = team.count('1')
    return count_0, count_1

def transform_team_data(teams):
    transformed = []
    for i, team in enumerate(teams):
        count_0, count_1 = count_team_results(team)
        transformed.append((team[0], -count_0, count_1, i))
    return transformed

def sort_teams(teams):
    return sorted(teams, key=operator.itemgetter(1, 2, 3))

def extract_team_names(teams):
    names = []
    for team in teams:
        names.append(team[0])
    return names

def print_team_names(names):
    print('\n'.join(names))

def process_block(file):
    n = read_number(file)
    if n == 0:
        return False
    teams = read_teams(file, n)
    transformed = transform_team_data(teams)
    sorted_teams = sort_teams(transformed)
    names = extract_team_names(sorted_teams)
    print_team_names(names)
    return True

def main():
    while True:
        if not process_block(f):
            break

main()