while True:
    input_values = list(map(int, input().split()))
    if not any(input_values):
        break
    sum_group_1 = input_values[0] + input_values[3]
    sum_group_2 = input_values[1] + input_values[4]
    sum_group_3 = input_values[2] + input_values[5]

    full_group_1, remaining_group_1 = divmod(sum_group_1, 3)
    full_group_2, remaining_group_2 = divmod(sum_group_2, 3)
    full_group_3, remaining_group_3 = divmod(sum_group_3, 3)

    full_groups_total = full_group_1 + full_group_2 + full_group_3
    remaining_groups = [remaining_group_1, remaining_group_2, remaining_group_3]
    max_remaining_group = max(remaining_groups)
    min_remaining_group = min(remaining_groups)
    count_two_remainders = remaining_groups.count(2)

    if max_remaining_group == 0:
        print(full_groups_total)
    elif max_remaining_group == 1:
        print(full_groups_total + min_remaining_group)
    elif max_remaining_group == 2:
        if count_two_remainders == 3:
            print(full_groups_total + 2)
        elif count_two_remainders == 2:
            for idx, (rem, full) in enumerate(zip(remaining_groups, [full_group_1, full_group_2, full_group_3])):
                if rem == 2:
                    continue
                if full == 0:
                    print(full_groups_total + rem)
                else:
                    print(full_groups_total + 1)
                break
        else:
            print(full_groups_total + min_remaining_group)