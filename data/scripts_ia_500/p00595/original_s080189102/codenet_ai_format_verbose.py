import fractions                                                                 

while True:

    try:
        input_string = raw_input()
        numerator, denominator = map(int, input_string.split())
    except EOFError:
        break

    greatest_common_divisor = fractions.gcd(numerator, denominator)
    print greatest_common_divisor