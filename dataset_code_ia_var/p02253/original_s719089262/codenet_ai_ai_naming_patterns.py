def schedule_selection_main():
    activity_count = int(input())
    activity_list = []
    for activity_index in range(activity_count):
        activity_list.append(list(map(int, input().split())))
    activity_list.sort(key=lambda activity: activity[1])
    selected_count = 0
    last_end_time = -1
    for activity_index in range(activity_count):
        if last_end_time < activity_list[activity_index][0]:
            last_end_time = activity_list[activity_index][1]
            selected_count += 1
    print(selected_count)

if __name__ == '__main__':
    schedule_selection_main()