input_values = list(map(int, open(0).read().split()))
count_items, *data_items = input_values
data_items.sort()

adjusted_values = [(24 - value) if index % 2 == 1 else value for index, value in enumerate(data_items)]
adjusted_values.append(0)

time_limit = 24
minimum_difference = min(
    abs(adjusted_values[i] - adjusted_values[j])
    for i in range(count_items + 1)
    for j in range(i + 1, count_items + 1)
)
print(minimum_difference)