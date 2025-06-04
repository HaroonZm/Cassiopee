input_steps_count = int(input())
position_ns = 0
position_ew = 0
directions_list = list(input())
for step_index in range(input_steps_count):
    ascii_value = ord(directions_list[step_index])
    if 65 <= ascii_value <= 77:
        position_ns += 1
    elif 78 <= ascii_value <= 90:
        position_ns -= 1
    elif 97 <= ascii_value <= 109:
        position_ew += 1
    else:
        position_ew -= 1
print(abs(position_ns) + abs(position_ew))
if position_ns > 0:
    print('A' * position_ns, sep='', end='')
elif position_ns < 0:
    print('Z' * (-position_ns), sep='', end='')
if position_ew > 0:
    print('a' * position_ew, sep='', end='')
elif position_ew < 0:
    print('z' * (-position_ew), sep='', end='')
print()