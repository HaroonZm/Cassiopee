height, num_operations = map(int, input().split())
row_states = [0] * height
for _ in range(num_operations):
    pos_x, pos_y = map(int, input().split())
    row_states[pos_y] += 2 ** pos_x

MASK_LEFT = 3
MASK_MIDDLE = 6
MASK_RIGHT = 12
MASK_ALL = 15

INFINITY = 10 ** 20
dp_table = [[-INFINITY] * 16 for _ in range(height + 1)]
dp_table[0][MASK_ALL] = 0

for row_index in range(height):
    current_state = row_states[row_index]
    for mask in (MASK_LEFT, MASK_MIDDLE, MASK_RIGHT):
        if current_state & mask:
            continue
        for previous_state in range(16):
            if previous_state & mask:
                continue
            new_state = current_state | mask
            dp_table[row_index + 1][new_state] = max(dp_table[row_index + 1][new_state], dp_table[row_index][previous_state] + 1)
    dp_table[row_index + 1][MASK_ALL] = max(dp_table[row_index + 1][MASK_ALL], -INFINITY if current_state else dp_table[row_index][0] + 2)
    dp_table[row_index + 1][current_state] = max(dp_table[row_index + 1][current_state], max(dp_table[row_index]))

print(max(dp_table[height]))