value_first, value_second = map(int, input().split())
sum_values = value_first + value_second
if sum_values < 24:
    print(sum_values)
else:
    print(sum_values - 24)