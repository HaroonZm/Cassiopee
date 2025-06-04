input_string = input()
repeat_count = int(input())

previous_char = ''
current_char_count = 1
group_sizes = []

first_char = input_string[0]
last_char = input_string[-1]

for current_char in input_string:
    if current_char == previous_char:
        current_char_count += 1
    elif previous_char == '':
        pass
    else:
        group_sizes.append(current_char_count)
        current_char_count = 1
    previous_char = current_char

group_sizes.append(current_char_count)

pair_count_once = 0
for group_size in group_sizes:
    pair_count_once += group_size // 2

if first_char == last_char and len(group_sizes) != 1:
    group_sizes[0] += group_sizes[-1]
    group_sizes.pop(-1)

pair_count_wrapped = 0
for group_size in group_sizes:
    pair_count_wrapped += group_size // 2

if len(input_string) == 1:
    print(repeat_count // 2)
elif len(group_sizes) == 1:
    print(repeat_count * len(input_string) // 2)
else:
    print(pair_count_once + pair_count_wrapped * (repeat_count - 1))