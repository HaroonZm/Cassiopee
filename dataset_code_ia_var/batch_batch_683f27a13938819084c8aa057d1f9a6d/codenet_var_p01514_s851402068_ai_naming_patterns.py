while True:
    num_teams, num_problems, num_records = map(int, input().split())
    if num_teams == 0 and num_problems == 0 and num_records == 0:
        break

    correct_matrix = [[0] * (num_problems + 1) for _ in range(num_teams + 1)]
    wrong_matrix = [[0] * (num_problems + 1) for _ in range(num_teams + 1)]
    penalty_list = [0] * (num_teams + 1)

    for record_idx in range(num_records):
        record_data = input().split()
        team_id = int(record_data[0])
        problem_id = int(record_data[1])
        submission_time = int(record_data[2])
        submission_status = record_data[3]

        if submission_status == 'WRONG':
            wrong_matrix[team_id][problem_id] += 1
        else:
            if correct_matrix[team_id][problem_id] == 0:
                correct_matrix[team_id][problem_id] = 1
                penalty_list[team_id] += wrong_matrix[team_id][problem_id] * 1200 + submission_time

    result_list = []
    for team_idx in range(1, num_teams + 1):
        solved_count = sum(correct_matrix[team_idx])
        total_penalty = penalty_list[team_idx]
        result_list.append((team_idx, solved_count, total_penalty))
        result_list.sort(key=lambda entry: (entry[1], -entry[2], -entry[0]), reverse=True)

    for result_idx in range(num_teams):
        print(result_list[result_idx][0], result_list[result_idx][1], result_list[result_idx][2])