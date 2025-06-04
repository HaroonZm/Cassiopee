size_value, weight_value = map(int, input().split())
if size_value <= weight_value:
    print('unsafe')
else:
    print('safe')