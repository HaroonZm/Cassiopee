user_input = input()
max_pattern_length = 0
if user_input[0] == user_input[1]:
    max_pattern_length = 1
for pattern_index in range(1, len(user_input) // 2):
    if pattern_index == len(user_input) // 2 - 1:
        break
    if user_input[:pattern_index] == user_input[pattern_index:2 * pattern_index]:
        max_pattern_length = pattern_index
print(2 * max_pattern_length)