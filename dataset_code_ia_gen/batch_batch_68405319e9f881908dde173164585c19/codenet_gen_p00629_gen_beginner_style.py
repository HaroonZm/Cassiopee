while True:
    n = int(input())
    if n == 0:
        break
    teams = []
    for _ in range(n):
        i,u,a,p = map(int,input().split())
        teams.append((i,u,a,p))
    # ソート：正解数降順、ペナルティ昇順、ID昇順
    teams.sort(key=lambda x:(-x[2], x[3], x[0]))
    selected = []
    count_per_school = {}
    for t in teams:
        team_id, school, solved, penalty = t
        total_selected = len(selected)
        c = count_per_school.get(school,0)
        if total_selected < 10:
            if c < 3:
                selected.append(team_id)
                count_per_school[school] = c + 1
        elif total_selected < 20:
            if c < 2:
                selected.append(team_id)
                count_per_school[school] = c + 1
        elif total_selected < 26:
            if c < 1:
                selected.append(team_id)
                count_per_school[school] = c + 1
        if len(selected) >= 26:
            break
    for sid in selected:
        print(sid)