input_n, input_a, input_b = map(int, input().split())
input_string = input()
max_total = input_a + input_b
current_total = 0
current_b_count = 0

for index in range(input_n):
    character = input_string[index]
    if character == 'a':
        if current_total < max_total:
            print('Yes')
            current_total += 1
        else:
            print('No')
    elif character == 'b':
        if current_total < max_total and current_b_count < input_b:
            current_total += 1
            current_b_count += 1
            print('Yes')
        else:
            print('No')
    else:
        print('No')