while True:

    number_of_teams = int(input())

    if number_of_teams == 0:
        break

    team_statistics_list = []

    for team_index in range(number_of_teams):

        row_tokens = input().split()
        team_name = row_tokens.pop(0)

        win_count = 0
        loss_count = 0

        for match_result in row_tokens:
            result_value = int(match_result)
            if result_value == 0:
                win_count += 1
            elif result_value == 1:
                loss_count += 1

        team_statistics_list.append((team_name, team_index, win_count, loss_count))

    sorted_teams = sorted(
        team_statistics_list,
        key=lambda team_stats: (-team_stats[2], team_stats[3], team_stats[1])
    )

    for team_stats in sorted_teams:
        print(team_stats[0])