from math import ceil as math_ceil

def main_loop():
    while True:
        try:
            input_value = float(input())
            gravity_constant = 9.8
            scaling_factor = 4.9
            offset_value = 5.0
            division_unit = 5.0

            time_value = input_value / gravity_constant
            result_y = scaling_factor * (time_value ** 2)
            result_n = math_ceil((result_y + offset_value) / division_unit)
            print(result_n)
        except EOFError:
            break

main_loop()