answer_count = 1

def count_consecutive_ones(data_list, current_index, current_count):
    global answer_count

    current_count += 1

    if data_list[current_index + 1] == 1:
        count_consecutive_ones(data_list, current_index + 1, current_count)
    elif answer_count <= current_count:
        answer_count = current_count + 1

input_size = int(input())
input_data_list = list(map(int, input().split()))
input_data_list.append(0)

for index in range(input_size):
    temp_count = 0
    if input_data_list[index] == 1:
        count_consecutive_ones(input_data_list, index, temp_count)

print(answer_count)