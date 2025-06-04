strength_value, weight_value = map(int, input().split())
if strength_value > weight_value:
    print('safe')
else:
    print('unsafe')