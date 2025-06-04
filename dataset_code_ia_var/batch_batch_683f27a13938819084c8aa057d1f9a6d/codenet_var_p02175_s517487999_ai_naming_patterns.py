value_initial, increment_a, increment_b = map(int, input().split())
operation_count = int(input())
for _ in range(operation_count):
    operation_type = input()
    if operation_type == "nobiro":
        value_initial = max(0, value_initial + increment_a)
    elif operation_type == "tidime":
        value_initial = max(0, value_initial + increment_b)
    else:
        value_initial = 0
print(value_initial)