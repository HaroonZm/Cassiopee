for iteration_index in range(input()):
    hex_input_value = int(raw_input(), 16)
    sign_bit_mask = 1 << 31
    result_sign_prefix = ""
    if hex_input_value & sign_bit_mask != 0:
        hex_input_value ^= sign_bit_mask
        result_sign_prefix = "-"
    float_value = hex_input_value * 1.0 / (1 << 7)
    integer_part = int(float_value)
    fractional_part = str(abs(float_value - integer_part))[1:]
    print result_sign_prefix + str(integer_part) + fractional_part