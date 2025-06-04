input_str = input()
result_count = 0
current_count = 0
for idx in range(3):
    if input_str[idx] == "R":
        current_count += 1
    else:
        result_count = max(result_count, current_count)
        current_count = 0
else:
    result_count = max(result_count, current_count)

print(result_count)