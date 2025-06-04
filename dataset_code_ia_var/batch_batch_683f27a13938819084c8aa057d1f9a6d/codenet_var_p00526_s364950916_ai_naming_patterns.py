input_count = int(input())
input_sequence = list(map(int, input().split()))
state_table = [[0]*3 for _ in range(input_count)]
state_table[0] = [1, 1, 1]
max_length = 0

for pos, (prev_value, curr_value) in enumerate(zip(input_sequence, input_sequence[1:]), start=1):
    if prev_value != curr_value:
        for state_idx in range(3):
            state_table[pos][state_idx] = state_table[pos-1][state_idx] + 1
    else:
        state_table[pos][0] = 1
        if state_table[pos-1][2] > max_length:
            max_length = state_table[pos-1][2]
        for state_idx in range(2, 0, -1):
            state_table[pos][state_idx] = state_table[pos-1][state_idx-1] + 1

print(max(max(state_table[-1]), max_length))