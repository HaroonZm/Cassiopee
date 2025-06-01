while True:
    number_of_players = int(input())
    if number_of_players == 0:
        break
    team_times_and_ids = []
    for _ in range(number_of_players):
        player_data = list(map(int, input().split()))
        player_id = player_data[0]
        split_times = player_data[1:]
        total_time_seconds = 0
        for minutes, seconds in zip(split_times[::2], split_times[1::2]):
            total_time_seconds += minutes * 60 + seconds
        team_times_and_ids.append((total_time_seconds, player_id))
    team_times_and_ids.sort()
    print(team_times_and_ids[0][1], team_times_and_ids[1][1], team_times_and_ids[-2][1], sep='\n')