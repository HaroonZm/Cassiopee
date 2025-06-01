import math

while True:
    
    try:
        first_integer, second_integer = map(int, input().split())
        greatest_common_divisor = math.gcd(first_integer, second_integer)
        print(greatest_common_divisor)
        
    except:
        break