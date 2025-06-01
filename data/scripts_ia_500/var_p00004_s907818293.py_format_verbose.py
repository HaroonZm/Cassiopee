import sys

for input_line in sys.stdin:
    
    coefficients = list(map(int, input_line.split()))
    
    coefficient_a = coefficients[0]
    coefficient_b = coefficients[1]
    coefficient_c = coefficients[2]
    coefficient_d = coefficients[3]
    coefficient_e = coefficients[4]
    coefficient_f = coefficients[5]

    denominator = (coefficient_a * coefficient_e) - (coefficient_b * coefficient_d)

    numerator_x = (coefficient_c * coefficient_e) - (coefficient_b * coefficient_f)
    numerator_y = (coefficient_a * coefficient_f) - (coefficient_c * coefficient_d)

    solution_x = numerator_x / denominator
    solution_y = numerator_y / denominator

    print("{0:.3f} {1:.3f}".format(solution_x, solution_y))