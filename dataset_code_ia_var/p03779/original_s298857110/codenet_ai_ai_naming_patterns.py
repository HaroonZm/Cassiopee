input_value = int(input())

current_number = 1

while current_number * (current_number + 1) // 2 < input_value:
    current_number += 1
print(current_number)