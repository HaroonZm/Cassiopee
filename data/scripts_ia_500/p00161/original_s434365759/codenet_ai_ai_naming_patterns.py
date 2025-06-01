while True:
    num_teams = int(input())
    if num_teams == 0:
        break
    team_times = {}
    for _ in range(num_teams):
        team_data = list(map(int, input().split()))
        team_id = team_data[0]
        total_time_seconds = 0
        for idx in range(1, 8, 2):
            minutes = team_data[idx]
            seconds = team_data[idx+1]
            total_time_seconds += 60 * minutes + seconds
        team_times[team_id] = total_time_seconds
    sorted_teams = sorted(team_times.items(), key=lambda item: item[1])
    print(sorted_teams[0][0], sorted_teams[1][0], sorted_teams[-2][0], sep='\n')