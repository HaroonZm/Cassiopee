numbers_list = []

for index in range(5):
    input_value = int(input())
    adjusted_value = input_value if input_value >= 40 else 40
    numbers_list.append(adjusted_value)

average_value = sum(numbers_list) // len(numbers_list)
print(average_value)