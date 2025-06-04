def read_team_count():
    return int(input())

def read_team_info():
    id, u, a, p = map(int, input().split())
    return (id, u, a, p)

def read_teams(n):
    teams = []
    for _ in range(n):
        teams.append(read_team_info())
    return teams

def sort_teams_by_criteria(teams):
    return sorted(teams, key=lambda x: (-x[2], x[3], x[0]))

def print_team_id(team, i):
    print(team[i][0])

def increment_total(total):
    return total + 1

def increment_affi(affi, u):
    affi[u] += 1
    return affi

def can_select_first_block(total, affi, u):
    return total < 10 and affi[u] < 3

def can_select_second_block(total, affi, u):
    return total < 20 and affi[u] < 2

def can_select_third_block(total, affi, u):
    return total < 26 and affi[u] < 1

def try_select_team(i, team, total, affi):
    u = team[i][1]
    if can_select_first_block(total, affi, u):
        return select_team(i, team, u, total, affi)
    elif can_select_second_block(total, affi, u):
        return select_team(i, team, u, total, affi)
    elif can_select_third_block(total, affi, u):
        return select_team(i, team, u, total, affi)
    return total, affi

def select_team(i, team, u, total, affi):
    print_team_id(team, i)
    total = increment_total(total)
    affi = increment_affi(affi, u)
    return total, affi

def process_teams(n, team):
    sorted_team = sort_teams_by_criteria(team)
    total = 0
    affi = [0]*1002
    for i in range(n):
        total, affi = try_select_team(i, sorted_team, total, affi)
    return

def process_one_case():
    n = read_team_count()
    if n == 0:
        return False
    team = read_teams(n)
    process_teams(n, team)
    return True

def main():
    while True:
        if not process_one_case():
            break

main()