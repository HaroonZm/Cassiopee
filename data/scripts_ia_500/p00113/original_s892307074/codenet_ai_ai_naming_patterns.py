while True:
    try:
        numerator, denominator = map(int, input().split())
    except:
        break
    remainder_positions = [-1] * denominator
    remainder_positions[numerator] = 0
    decimal_representation = ''
    for position in range(1, denominator):
        numerator *= 10
        decimal_digit = numerator // denominator
        decimal_representation += str(decimal_digit)
        remainder = numerator % denominator
        if remainder == 0 or remainder_positions[remainder] >= 0:
            print(decimal_representation)
            if remainder_positions[remainder] >= 0:
                print(*[' '] * remainder_positions[remainder], *['^'] * (position - remainder_positions[remainder]), sep='')
            break
        remainder_positions[remainder], numerator = position, remainder