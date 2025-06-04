while True:
    num_teams, num_problems, num_records = map(int, raw_input().split())
    if num_teams == num_problems == num_records == 0:
        break

    incorrect_attempts = [[0 for problem_idx in xrange(num_problems)] for team_idx in xrange(num_teams)]
    penalty_times = [[0 for problem_idx in xrange(num_problems)] for team_idx in xrange(num_teams)]

    for record_idx in xrange(num_records):
        team_id_str, problem_id_str, submission_time_str, result_str = raw_input().split()
        team_idx = int(team_id_str) - 1
        problem_idx = int(problem_id_str) - 1
        submission_time = int(submission_time_str)
        if penalty_times[team_idx][problem_idx] == 0:
            if result_str == 'CORRECT':
                penalty_times[team_idx][problem_idx] = incorrect_attempts[team_idx][problem_idx] * 1200 + submission_time
            else:
                incorrect_attempts[team_idx][problem_idx] += 1

    team_results = []
    for team_idx in xrange(num_teams):
        solved_count = sum(1 for penalty in penalty_times[team_idx] if penalty != 0)
        total_penalty = sum(penalty_times[team_idx])
        team_number = team_idx + 1
        # Negative because sort by descending solved, then ascending penalty, then ascending team number
        team_results.append((-solved_count, total_penalty, team_number))

    team_results.sort()

    for result_tuple in team_results:
        team_number = result_tuple[2]
        solved_count = -result_tuple[0]
        total_penalty = result_tuple[1]
        print team_number, solved_count, total_penalty