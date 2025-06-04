input_size = int(input())
input_values = list(map(int, input().split()))
left_pointer = 1
right_pointer = 2 * input_size

while left_pointer < right_pointer - 1:
    mid_value = (left_pointer + right_pointer) // 2
    is_ge_mid = []
    is_same_group = []
    for index in range(0, 2 * input_size - 1):
        is_ge_mid.append(input_values[index] >= mid_value)
        is_same_group.append(0)
    for index in range(1, 2 * input_size - 1):
        if is_ge_mid[index - 1] == is_ge_mid[index]:
            is_same_group[index] = 1
    for index in range(0, 2 * input_size - 2):
        if is_ge_mid[index + 1] == is_ge_mid[index]:
            is_same_group[index] = 1
    min_distance = 2 * input_size
    answer_found = False
    for index in range(0, 2 * input_size - 1):
        if is_same_group[index] == 1:
            if abs(index - input_size + 1) < min_distance:
                min_distance = abs(index - input_size + 1)
                answer_found = is_ge_mid[index]
    if min_distance == 2 * input_size:
        answer_found = ((input_size + 1) % 2) ^ is_ge_mid[input_size - 1]
    if answer_found is True:
        left_pointer = mid_value
    else:
        right_pointer = mid_value
print(left_pointer)