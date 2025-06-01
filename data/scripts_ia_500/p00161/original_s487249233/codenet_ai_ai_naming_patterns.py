while True:
    number_of_entries = int(input())
    if number_of_entries == 0:
        break
    time_score_index_list = []
    for _ in range(number_of_entries):
        runner_id, m1, s1, m2, s2, m3, s3, m4, s4 = map(int, input().split())
        total_seconds = (m1 + m2 + m3 + m4) * 60 + (s1 + s2 + s3 + s4)
        time_score_index_list.append((total_seconds, runner_id))
    time_score_index_list.sort()
    print(time_score_index_list[0][1])
    print(time_score_index_list[1][1])
    print(time_score_index_list[-2][1])