def read_int_list(): 
    return list(map(int, input().split()))

CONST_MODULO = 10 ** 9 + 7

value_a, value_b, value_x = read_int_list()
if value_x < value_a:
    print(value_x % CONST_MODULO)
else:
    value_e = (value_x - value_b) // (value_a - value_b)
    print((value_x + value_e * value_b) % CONST_MODULO)