first_value, second_value = map(int, raw_input().split())
if first_value > second_value:
    print 'first_value > second_value'
elif first_value < second_value:
    print 'first_value < second_value'
elif first_value == second_value:
    print 'first_value == second_value'