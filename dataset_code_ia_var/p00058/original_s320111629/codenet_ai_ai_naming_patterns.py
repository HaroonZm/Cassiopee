import sys
for input_line in sys.stdin:
    value_a, value_b, value_c, value_d, value_e, value_f, value_g, value_h = map(float, input_line.split())
    scalar_product_result = (value_c - value_a) * (value_g - value_e) + (value_d - value_b) * (value_h - value_f)
    is_perpendicular = abs(scalar_product_result) < 1e-10
    output_message = "YES" if is_perpendicular else "NO"
    print output_message