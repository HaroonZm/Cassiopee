while True:
    
    decimal_number = float(input())
    
    if decimal_number < 0:
        break
    
    integer_part = int(decimal_number)
    fractional_part = decimal_number - integer_part
    
    binary_representation = bin(integer_part)[2:].zfill(8) + '.'
    
    for _ in range(4):
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