input_count = int(input())
input_list = list(map(int, input().split()))

max_value = max(input_list)
second_value = 0

for index in range(input_count):
    current_value = input_list[index]
    if current_value != max_value:
        if abs(current_value * 2 - max_value) < abs(second_value * 2 - max_value):
            second_value = current_value

print(max_value, end=' ')
print(second_value)