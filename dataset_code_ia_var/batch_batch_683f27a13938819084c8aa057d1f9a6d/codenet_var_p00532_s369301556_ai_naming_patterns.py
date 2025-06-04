count_list = [0] * int(input())
num_rounds = int(input())
targets_list = list(map(int, input().split()))

for round_idx in range(num_rounds):
    current_target = targets_list[round_idx]
    response_list = list(map(int, input().split()))
    for response_idx, response_value in enumerate(response_list):
        if response_value == current_target:
            count_list[response_idx] += 1
    count_list[current_target - 1] += len(count_list) - response_list.count(current_target)

for count_value in count_list:
    print(count_value)