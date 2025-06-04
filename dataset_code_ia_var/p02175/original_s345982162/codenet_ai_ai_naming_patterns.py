value_x, value_a, value_b = map(int, input().split())
input_count = int(input())
input_list = [input() for _ in range(input_count)]

for input_item in input_list:
    if input_item == 'nobiro':
        value_x += value_a
    elif input_item == 'tidime':
        value_x += value_b
    else:
        value_x = 0
    if value_x < 0:
        value_x = 0
print(value_x)