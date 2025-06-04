max_one_sequence_length = 1

def update_one_sequence_count(arr, idx, current_count):
    global max_one_sequence_length
    current_count += 1
    if arr[idx + 1] == 1:
        update_one_sequence_count(arr, idx + 1, current_count)
    elif max_one_sequence_length <= current_count:
        max_one_sequence_length = current_count + 1

input_size = int(input())
input_sequence = list(map(int, input().split()))
input_sequence.append(0)

for seq_idx in range(input_size):
    sequence_count = 0
    if input_sequence[seq_idx] == 1:
        update_one_sequence_count(input_sequence, seq_idx, sequence_count)

print(max_one_sequence_length)