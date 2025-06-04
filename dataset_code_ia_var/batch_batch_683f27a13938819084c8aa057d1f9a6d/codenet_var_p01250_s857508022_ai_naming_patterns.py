from math import pi as math_pi
while True:
    radius_tolerance = float(input())
    if radius_tolerance == 0:
        break
    numerator_value = 1
    denominator_value = 1
    while abs(numerator_value / denominator_value - math_pi) > radius_tolerance:
        if numerator_value / denominator_value < math_pi:
            numerator_value += 1
        else:
            denominator_value += 1
    print('%d/%d' % (numerator_value, denominator_value))