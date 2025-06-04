import sys
import itertools

for input_line in sys.stdin:
    try:
        numerator, denominator = map(int, input_line.split())
    except ValueError:
        break
    
    quotient, remainder = divmod(numerator, denominator)
    remainder *= 10
    
    remainder_positions = {remainder: 0}
    digits_result = ''
    
    for index in itertools.count(1):
        digit, remainder = divmod(remainder, denominator)
        remainder *= 10
        digits_result += str(digit)
        
        if remainder == 0:
            print(digits_result)
            break
        
        if remainder in remainder_positions:
            print(digits_result)
            start_index = remainder_positions[remainder]
            print(' ' * start_index + '^' * (index - start_index))
            break
        
        remainder_positions[remainder] = index