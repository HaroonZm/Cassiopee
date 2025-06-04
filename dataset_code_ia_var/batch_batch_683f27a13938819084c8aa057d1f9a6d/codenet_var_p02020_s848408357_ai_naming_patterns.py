input_n = int(input())
input_sequence = list(map(int, input().split()))
sorted_sequence_desc = sorted(input_sequence, reverse=True)
sum_result = 0
carry_over = 0

for current_value in sorted_sequence_desc:
    if current_value % 2 == 0:
        sum_result += current_value // 2
    elif carry_over != 0:
        sum_result += (carry_over + current_value) // 2
        carry_over = 0
    else:
        carry_over = current_value

print(sum_result)