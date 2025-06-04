input_length = int(input())
input_sequence = list(map(int, input().split()))

dp_table = [[1] * 3 for dp_row_index in range(input_length)]
max_length = 1
for current_index in range(input_length - 1):
    for equal_allowed_count in range(3):
        if input_sequence[current_index] != input_sequence[current_index + 1]:
            if dp_table[current_index + 1][equal_allowed_count] < dp_table[current_index][equal_allowed_count] + 1:
                dp_table[current_index + 1][equal_allowed_count] = dp_table[current_index][equal_allowed_count] + 1
        if equal_allowed_count < 2 and input_sequence[current_index] == input_sequence[current_index + 1]:
            if dp_table[current_index + 1][equal_allowed_count + 1] < dp_table[current_index][equal_allowed_count] + 1:
                dp_table[current_index + 1][equal_allowed_count + 1] = dp_table[current_index][equal_allowed_count] + 1
for dp_row in dp_table:
    current_max = max(dp_row)
    if max_length < current_max:
        max_length = current_max
print(max_length)