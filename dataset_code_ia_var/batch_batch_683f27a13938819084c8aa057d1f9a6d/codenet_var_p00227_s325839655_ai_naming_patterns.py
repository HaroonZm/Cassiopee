while True:
    try:
        input_count, input_group = map(int, input().split())
        value_list = list(map(int, input().split()))
        value_list.sort(reverse=True)
        for group_index in range(input_group - 1, input_count, input_group):
            value_list[group_index] = 0
        print(sum(value_list))
    except:
        break