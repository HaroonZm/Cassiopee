import sys

for input_line in sys.stdin:
    coeff_a, coeff_b, const_c, coeff_d, coeff_e, const_f = map(int, input_line.split())
    denominator = coeff_a * coeff_e - coeff_b * coeff_d
    numerator_x = const_c * coeff_e - coeff_b * const_f
    numerator_y = coeff_a * const_f - const_c * coeff_d
    solution_x = numerator_x / denominator
    solution_y = numerator_y / denominator
    print("{0:.3f} {1:.3f}".format(solution_x, solution_y))