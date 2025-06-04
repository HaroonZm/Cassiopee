value_base, value_increment_a, value_increment_b = map(int, input().split())
operation_count = int(input())
for operation_index in range(operation_count):
    operation_type = input()
    if operation_type == 'nobiro':
        value_base += value_increment_a
        if value_base < 0:
            value_base = 0
    elif operation_type == 'tidime':
        value_base += value_increment_b
        if value_base < 0:
            value_base = 0
    else:
        value_base = 0
print(value_base)