while True:
    try:
        coef_a, coef_b, coef_c, coef_d, coef_e, coef_f = map(int, input().split())
        denominator = coef_b * coef_d - coef_a * coef_e
        value_y = (coef_c * coef_d - coef_a * coef_f) / denominator
        value_x = (coef_c - coef_b * value_y) / coef_a
        print("{:.3f} {:.3f}".format(value_x, value_y))
    except:
        break