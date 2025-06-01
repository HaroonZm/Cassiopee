def calculate_gcd(first_number, second_number):
    
    remainder = second_number % first_number
    
    if first_number % remainder == 0:
        return remainder
    else:
        return calculate_gcd(remainder, first_number)


while True:
    
    try:
        input_numbers = input().split()
        first_number, second_number = list(map(float, input_numbers))
    except EOFError:
        break
    
    if first_number >= second_number:
        first_number, second_number = second_number, first_number
    
    if second_number % first_number != 0:
        greatest_common_divisor = calculate_gcd(first_number, second_number)
    else:
        greatest_common_divisor = first_number
    
    least_common_multiple = int(first_number * second_number / greatest_common_divisor)
    
    print("{0} {1}".format(int(greatest_common_divisor), least_common_multiple))