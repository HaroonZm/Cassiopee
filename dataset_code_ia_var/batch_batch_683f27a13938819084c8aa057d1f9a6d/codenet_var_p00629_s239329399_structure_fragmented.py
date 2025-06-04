def swap_teams(teams, i, j):
    tmp = teams[i]
    teams[i] = teams[j]
    teams[j] = tmp

def compare_by_points(t1, t2):
    return t1[2] < t2[2]

def compare_by_second_criteria(t1, t2):
    return t1[3] > t2[3]

def compare_by_third_criteria(t1, t2):
    return t1[3] == t2[3] and t1[0] > t2[0]

def should_swap(t1, t2):
    if compare_by_points(t1, t2):
        return True
    if t1[2] == t2[2]:
        if compare_by_second_criteria(t1, t2):
            return True
        if compare_by_third_criteria(t1, t2):
            return True
    return False

def bubble_pass(teams, n, i):
    for j in range(n - i - 1):
        if should_swap(teams[j], teams[j + 1]):
            swap_teams(teams, j, j + 1)

def team_sort(teams, n):
    for i in range(n - 1):
        bubble_pass(teams, n, i)

def init_selection():
    return []

def init_count():
    return {}

def get_group_str(team):
    return str(team[1])

def can_select(selection, count, group, limit):
    return len(selection) < limit and count[group] < selection_limit_per_group(limit)

def selection_limit_per_group(limit):
    if limit <= 10:
        return 3
    elif limit <= 20:
        return 2
    else:
        return 1

def current_limit(selection_length):
    if selection_length < 10:
        return 10
    elif selection_length < 20:
        return 20
    elif selection_length < 26:
        return 26
    else:
        return None

def try_select(selection, count, team):
    group = get_group_str(team)
    count.setdefault(group, 0)
    limit = current_limit(len(selection))
    if limit is not None and count[group] < selection_limit_per_group(limit):
        selection.append(team)
        count[group] += 1

def process_selection(teams):
    selection = init_selection()
    count = init_count()
    for team in teams:
        if len(selection) >= 26:
            break
        try_select(selection, count, team)
    return selection

def print_selected(teams):
    for t in teams:
        print(t[0])

def select(teams):
    selected = process_selection(teams)
    print_selected(selected)

def read_team():
    t = [int(x) for x in input().split()]
    return t

def read_teams(n):
    teams = []
    for i in range(n):
        teams.append(read_team())
    return teams

def process(n):
    teams = read_teams(n)
    team_sort(teams, n)
    select(teams)

def main_loop():
    while True:
        n = int(input())
        if n == 0:
            break
        process(n)

main_loop()