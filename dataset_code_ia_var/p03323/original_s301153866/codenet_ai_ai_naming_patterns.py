input_value_first, input_value_second = map(int, input().split())
maximum_value = max(input_value_first, input_value_second)
limit_value = 8
if maximum_value > limit_value:
    print(':(')
else:
    print('Yay!')