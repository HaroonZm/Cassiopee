while True:
    input_event_count = int(input())
    if input_event_count == 0:
        break

    day_participants_list = [[] for day_index in range(31)]
    participant_meet_sets = [set() for participant_index in range(input_event_count)]

    for participant_index in range(input_event_count):
        input_line = list(map(int, input().split()))
        for day in input_line[1:]:
            day_participants_list[day].append(participant_index)

    for day_index in range(31):
        union_meet_set = set()
        for participant in day_participants_list[day_index]:
            union_meet_set |= participant_meet_sets[participant]
        for participant in day_participants_list[day_index]:
            participant_meet_sets[participant] = union_meet_set | set(day_participants_list[day_index])
            if len(participant_meet_sets[participant]) == input_event_count:
                break
        else:
            continue
        break
    else:
        print(-1)
        continue
    print(day_index)