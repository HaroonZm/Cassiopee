while True:
    user_input = float(input())
    if user_input < 0:
        break
    fractional_part = user_input - int(user_input)
    binary_representation = bin(int(user_input))[2:].zfill(8) + '.'
    for fractional_index in range(4):
        fractional_part *= 2
        if fractional_part >= 1:
            binary_representation += '1'
            fractional_part -= 1
        else:
            binary_representation += '0'
    if fractional_part > 1e-10 or len(binary_representation) > 13:
        print('NA')
    else:
        print(binary_representation)