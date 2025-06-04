naming_digits_chars = "-0123456789"

def naming_cross_point_func(coords_P, coords_Q):
    px0, py0, px1, py1 = coords_P
    qx0, qy0, qx1, qy1 = coords_Q
    pdx = px1 - px0
    pdy = py1 - py0
    qdx = qx1 - qx0
    qdy = qy1 - qy0

    det_s = (py0 - qy0) * qdx - (px0 - qx0) * qdy
    det_sm = pdx * qdy - pdy * qdx
    if det_s < 0:
        det_s = -det_s
        det_sm = -det_sm
    if det_s == 0:
        cross_x = px0
        cross_y = py0
    else:
        cross_x = px0 + det_s * pdx / det_sm
        cross_y = py0 + det_s * pdy / det_sm
    return cross_x, cross_y

def naming_reflection_func(ref_line, ref_point):
    line_x0, line_y0, line_x1, line_y1 = ref_line
    point_x, point_y = ref_point
    dx = line_x1 - line_x0
    dy = line_y1 - line_y0
    rel_px = point_x - line_x0
    rel_py = point_y - line_y0
    val_cv = rel_px * dx + rel_py * dy
    val_sv = rel_px * dy - rel_py * dx
    cv_sq_diff = val_cv ** 2 - val_sv ** 2
    sv_twice_cv_sv = 2 * val_cv * val_sv
    denom_dd = (rel_px ** 2 + rel_py ** 2) * (dx ** 2 + dy ** 2)
    if denom_dd == 0:
        return line_x0 + rel_px, line_y0 + rel_py
    result_x = line_x0 + (cv_sq_diff * rel_px - sv_twice_cv_sv * rel_py) / denom_dd
    result_y = line_y0 + (sv_twice_cv_sv * rel_px + cv_sq_diff * rel_py) / denom_dd
    return result_x, result_y

def naming_parse_expr_func(expression_string):
    parsing_string = expression_string + "$"
    parsing_index = 0

    def parse_expr():
        nonlocal parsing_index
        result_expr = None
        while parsing_string[parsing_index] == '(':
            parsing_index += 1
            if parsing_string[parsing_index] in naming_digits_chars:
                num_x = parse_number()
                parsing_index += 1
                num_y = parse_number()
                next_expr = (0, num_x, num_y)
            else:
                next_expr = parse_expr()
            parsing_index += 1
            if result_expr is None:
                result_expr = next_expr
            else:
                if result_expr[0] == next_expr[0] == 0:
                    result_expr = (1, result_expr[1], result_expr[2], next_expr[1], next_expr[2])
                elif result_expr[0] == next_expr[0] == 1:
                    cr_x, cr_y = naming_cross_point_func(result_expr[1:], next_expr[1:])
                    result_expr = (0, cr_x, cr_y)
                else:
                    if result_expr[0] == 0:
                        point_dat, line_dat = result_expr, next_expr
                    else:
                        point_dat, line_dat = next_expr, result_expr
                    ref_x, ref_y = naming_reflection_func(line_dat[1:], point_dat[1:])
                    result_expr = (0, ref_x, ref_y)
            if parsing_string[parsing_index] != '@':
                break
            parsing_index += 1
        return result_expr

    def parse_number():
        nonlocal parsing_index
        value_num = 0
        is_negative = False
        if parsing_string[parsing_index] == '-':
            is_negative = True
            parsing_index += 1
        while parsing_string[parsing_index] in naming_digits_chars:
            value_num = 10 * value_num + int(parsing_string[parsing_index])
            parsing_index += 1
        return -value_num if is_negative else value_num

    return parse_expr()

def naming_solve_func():
    input_line_str = input()
    if input_line_str == '#':
        return False
    result_val = naming_parse_expr_func(input_line_str)
    print("%.16f %.16f" % result_val[1:])
    return True

while naming_solve_func():
    pass