while True:
    num_teams, num_problems, num_records = map(int, input().split())
    if num_teams == 0:
        break

    teams_stats = [[0 for _ in range(3)] for _ in range(num_teams)]  # [team_id, problems_solved, total_penalty]
    wrong_attempts = [[0 for _ in range(num_problems)] for _ in range(num_teams)]
    for team_idx in range(num_teams):
        teams_stats[team_idx][0] = team_idx + 1

    for _ in range(num_records):
        record = input().split()
        team_idx = int(record[0]) - 1
        problem_idx = int(record[1]) - 1
        submit_time = int(record[2])
        verdict = record[3]

        if verdict == "CORRECT":
            teams_stats[team_idx][1] += 1
            teams_stats[team_idx][2] += (wrong_attempts[team_idx][problem_idx] * 1200 + submit_time)
        else:
            wrong_attempts[team_idx][problem_idx] += 1

    teams_stats.sort(key=lambda team: (-team[1], team[2], team[0]))
    for team_data in teams_stats:
        print(' '.join(str(stat) for stat in team_data))