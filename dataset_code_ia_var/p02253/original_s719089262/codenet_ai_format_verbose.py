def main():
    number_of_activities = int(input())

    activity_schedule = []

    for _ in range(number_of_activities):
        start_and_end_times = list(map(int, input().split()))
        activity_schedule.append(start_and_end_times)

    activity_schedule.sort(key=lambda activity: activity[1])

    maximum_non_overlapping_activities = 0
    last_activity_end_time = -1

    for activity_index in range(number_of_activities):
        activity_start_time = activity_schedule[activity_index][0]
        activity_end_time = activity_schedule[activity_index][1]

        if last_activity_end_time < activity_start_time:
            last_activity_end_time = activity_end_time
            maximum_non_overlapping_activities += 1

    print(maximum_non_overlapping_activities)

if __name__ == '__main__':
    main()