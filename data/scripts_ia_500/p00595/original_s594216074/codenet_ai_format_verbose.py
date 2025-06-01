def calculate_greatest_common_divisor(dividend, divisor):
    
    if dividend % divisor == 0:
        return divisor
    
    return dividend % divisor


while True:
    try:
        first_number, second_number = map(int, raw_input().split())
    except EOFError:
        break

    while first_number != second_number:
        
        if first_number > second_number:
            first_number = calculate_greatest_common_divisor(first_number, second_number)
        
        elif second_number > first_number:
            second_number = calculate_greatest_common_divisor(second_number, first_number)
            
    print first_number