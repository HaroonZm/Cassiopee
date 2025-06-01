length, steps = [int(value) for value in input().split()]
snake_pattern = input()

consecutive_o_count = 0
for index in range(length - 1):
    if snake_pattern[index] == "o" and snake_pattern[index + 1] == "o":
        consecutive_o_count += 1

total_length = length
for _ in range(steps):
    total_length += consecutive_o_count * 3
    consecutive_o_count *= 2

print(total_length)