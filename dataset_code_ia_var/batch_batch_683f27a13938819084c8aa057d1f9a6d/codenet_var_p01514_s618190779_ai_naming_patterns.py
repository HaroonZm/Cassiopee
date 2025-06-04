num_teams, num_problems, num_records = map(int, raw_input().split())
while num_teams != 0:
    team_penalties = [0] * num_teams
    team_solved = [0] * num_teams
    team_published = [[False] * num_problems for _ in range(num_teams)]
    team_mistakes = [[0] * num_problems for _ in range(num_teams)]
    for _ in range(num_records):
        record_team, record_problem, record_time, record_message = raw_input().split()
        team_idx = int(record_team) - 1
        problem_idx = int(record_problem) - 1
        solve_time = int(record_time)
        if team_published[team_idx][problem_idx]:
            continue
        if record_message == "CORRECT":
            team_published[team_idx][problem_idx] = True
            team_penalties[team_idx] += team_mistakes[team_idx][problem_idx] * 1200 + solve_time
            team_solved[team_idx] += 1
        else:
            team_mistakes[team_idx][problem_idx] += 1
    ranking = []
    for team_id in range(num_teams):
        ranking.append([-team_solved[team_id], team_penalties[team_id], team_id])
    ranking.sort()
    for entry in ranking:
        print entry[2] + 1, -entry[0], entry[1]
    num_teams, num_problems, num_records = map(int, raw_input().split())