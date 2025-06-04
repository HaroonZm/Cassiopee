def get_number_of_teams():
    return int(input())

def get_team_input():
    return list(map(int, input().split()))

def collect_teams(n):
    teams = []
    for _ in range(n):
        teams.append(get_team_input())
    return teams

def sort_by_first(teams):
    return sorted(teams, key=lambda x: x[0])

def sort_by_fourth(teams):
    return sorted(teams, key=lambda x: x[3])

def sort_by_third_reverse(teams):
    return sorted(teams, key=lambda x: x[2], reverse=True)

def multi_sort(teams):
    teams1 = sort_by_first(teams)
    teams2 = sort_by_fourth(teams1)
    teams3 = sort_by_third_reverse(teams2)
    return teams3

def count_team_number(ans, team_num):
    count = 0
    for t in ans:
        if t[1] == team_num:
            count += 1
    return count

def can_add_first_section(ans, e):
    return len(ans) < 10 and count_team_number(ans, e[1]) < 3

def can_add_second_section(ans, e):
    return len(ans) < 20 and count_team_number(ans, e[1]) < 2

def can_add_third_section(ans, e):
    return len(ans) < 26 and count_team_number(ans, e[1]) == 0

def should_add(ans, e):
    return (
        can_add_first_section(ans, e) or
        can_add_second_section(ans, e) or
        can_add_third_section(ans, e)
    )

def build_answer(rank):
    ans = []
    for e in rank:
        if should_add(ans, e):
            ans.append(e)
    return ans

def print_answers(ans):
    for a in ans:
        print(a[0])

def process_group(n):
    teams = collect_teams(n)
    rank = multi_sort(teams)
    ans = build_answer(rank)
    print_answers(ans)

def main_loop():
    while True:
        n = get_number_of_teams()
        if n == 0:
            break
        process_group(n)

def main():
    main_loop()

if __name__ == "__main__":
    main()