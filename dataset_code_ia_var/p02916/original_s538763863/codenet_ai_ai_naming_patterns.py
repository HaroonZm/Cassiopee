input_length = int(input())
index_list = [value-1 for value in map(int, input().split())]
main_values = list(map(int, input().split()))
bonus_values = list(map(int, input().split()))

total_sum = 0
previous_index = -100
for position in range(input_length):
    current_index = index_list[position]
    total_sum += main_values[current_index]
    if previous_index == current_index - 1:
        total_sum += bonus_values[previous_index]
    previous_index = current_index

print(total_sum)