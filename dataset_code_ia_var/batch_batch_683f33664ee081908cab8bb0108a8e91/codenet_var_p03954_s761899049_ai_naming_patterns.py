input_count = int(input())
input_list = list(map(int, input().split()))
range_left, range_right = 1, input_count * 2

while range_right - range_left > 1:
    range_middle = (range_left + range_right) // 2
    marker_list = [0] * (2 * input_count - 1)
    for marker_index in range(2 * input_count - 1):
        if input_list[marker_index] >= range_middle:
            marker_list[marker_index] = 1
    pivot_value = marker_list[input_count - 1]
    for offset in range(input_count - 1):
        condition_forward = (pivot_value + marker_list[input_count + offset] + offset) & 1 == 0
        if condition_forward:
            if marker_list[input_count + offset] & 1:
                range_left = range_middle
            else:
                range_right = range_middle
            break
        condition_backward = (pivot_value + marker_list[input_count - offset - 2] + offset) & 1 == 0
        if condition_backward:
            if marker_list[input_count - offset - 2] & 1:
                range_left = range_middle
            else:
                range_right = range_middle
            break
    else:
        if (input_count + pivot_value) & 1:
            range_right = range_middle
        else:
            range_left = range_middle
print(range_left)