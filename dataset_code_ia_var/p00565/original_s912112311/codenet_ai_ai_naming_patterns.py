input_count = int(input())
sequence_values = list(map(int, input().split()))
max_consecutive_ones = 0
current_consecutive_ones = 0
for value in sequence_values:
    if value == 1:
        current_consecutive_ones += 1
        if current_consecutive_ones > max_consecutive_ones:
            max_consecutive_ones = current_consecutive_ones
    else:
        current_consecutive_ones = 0
required_dice_faces = max_consecutive_ones + 1
print(required_dice_faces)