user_target_value, forbidden_values_count = map(int, input().split())

forbidden_values_list = list(map(int, input().split()))

if len(forbidden_values_list) == 0:
    print(user_target_value)
    exit()

for difference_from_target in range(forbidden_values_count + 1):

    candidate_value_below = user_target_value - difference_from_target

    if forbidden_values_list.count(candidate_value_below) == 0:
        print(candidate_value_below)
        exit()

    candidate_value_above = user_target_value + difference_from_target

    if forbidden_values_list.count(candidate_value_above) == 0:
        print(candidate_value_above)
        exit()