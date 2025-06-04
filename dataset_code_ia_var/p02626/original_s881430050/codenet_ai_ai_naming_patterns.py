num_elements = int(input())
input_list = list(map(int, input().split()))
xor_total = 0

if num_elements == 2:
    first_value, second_value = input_list
    if first_value >= second_value and (first_value + second_value) % 2 == 0:
        print((first_value + second_value) // 2 - second_value)
    else:
        print(-1)
    exit()

for index_element in range(2, num_elements):
    xor_total ^= input_list[index_element]

first_value, second_value = input_list[0], input_list[1]
sum_pair = first_value + second_value
bit_pattern_list = []
current_sum = 0

for bit_position in range(49, -1, -1):
    if xor_total & (1 << bit_position):
        bit_pattern_list.append(1)
        current_sum += (1 << bit_position)
    else:
        if current_sum + (2 << bit_position) > sum_pair:
            bit_pattern_list.append(0)
        else:
            bit_pattern_list.append(2)
            current_sum += (2 << bit_position)

if current_sum != sum_pair:
    print(-1)
    exit()

min_value = 0
max_value = 0

for bit_index in range(50):
    pattern_value = bit_pattern_list[bit_index]
    if pattern_value == 1:
        max_value += (1 << (49 - bit_index))
    elif pattern_value == 2:
        min_value += (1 << (49 - bit_index))
        max_value += (1 << (49 - bit_index))

if not (min_value <= first_value):
    print(-1)
    exit()

final_answer = min_value

for bit_index in range(50):
    if bit_pattern_list[bit_index] == 1:
        increment_value = (1 << (49 - bit_index))
        if final_answer + increment_value > first_value:
            continue
        else:
            final_answer += increment_value

if final_answer == 0:
    print(-1)
else:
    print(first_value - final_answer)