def get_input_team():
    return list(map(int, raw_input().split()))

def get_all_teams(n):
    teams = []
    for _ in range(n):
        teams.append(get_input_team())
    return teams

def sort_key(team):
    return -1e12 * team[2] + team[3] * 1e6 + team[0]

def sort_teams(teams):
    return sorted(teams, key=sort_key)

def update_threshold(a_length):
    if a_length == 10:
        return 2
    elif a_length == 20:
        return 1
    else:
        return 3

def can_add_team(B, member, threshold):
    return B.count(member) < threshold

def check_finish(a_length):
    return a_length == 26

def process_teams(teams):
    A = []
    B = []
    threshold = 3
    for team in teams:
        threshold = update_threshold(len(A))
        if can_add_team(B, team[1], threshold):
            A.append(team[0])
            B.append(team[1])
        if check_finish(len(A)):
            break
    return A

def print_results(A):
    for a in A:
        print(a)

def handle_case(n):
    teams = get_all_teams(n)
    sorted_teams = sort_teams(teams)
    result_A = process_teams(sorted_teams)
    print_results(result_A)

def read_n():
    return int(raw_input())

def main_loop():
    while True:
        n = read_n()
        if n == 0:
            break
        handle_case(n)

main_loop()