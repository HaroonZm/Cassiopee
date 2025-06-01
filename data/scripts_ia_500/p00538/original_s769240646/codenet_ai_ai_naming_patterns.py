import sys
sys.setrecursionlimit(100000)

num_elements, *value_list = map(int, open(0).read().split())
dp_table = [[-1] * num_elements for index in range(num_elements)]

for index in range(num_elements):
    dp_table[index][index] = value_list[index] if num_elements % 2 else 0

def compute_max_score(left_index, right_index, turn_flag):
    if dp_table[left_index][right_index] != -1:
        return dp_table[left_index][right_index]
    if turn_flag:
        take_left = value_list[left_index] + compute_max_score((left_index + 1) % num_elements, right_index, 0)
        take_right = value_list[right_index] + compute_max_score(left_index, (right_index - 1) % num_elements, 0)
        dp_table[left_index][right_index] = max(take_left, take_right)
    else:
        if value_list[left_index] < value_list[right_index]:
            dp_table[left_index][right_index] = compute_max_score(left_index, (right_index - 1) % num_elements, 1)
        else:
            dp_table[left_index][right_index] = compute_max_score((left_index + 1) % num_elements, right_index, 1)
    return dp_table[left_index][right_index]

max_score = 0
for start_index in range(num_elements):
    score = value_list[start_index] + compute_max_score((start_index + 1) % num_elements, (start_index - 1) % num_elements, 0)
    if score > max_score:
        max_score = score

print(max_score)