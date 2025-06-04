ship_weight, weight_limit = map(int, input().split())

if ship_weight <= weight_limit:
    print('unsafe')
else:
    print('safe')