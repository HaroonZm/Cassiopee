num_range, num_center = map(int, input().split())

for value_current in range(num_center - num_range + 1, num_center + num_range):
    print(value_current)