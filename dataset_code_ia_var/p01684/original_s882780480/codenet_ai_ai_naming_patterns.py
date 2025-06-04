import sys
input_read = sys.stdin.readline
output_write = sys.stdout.write

from math import pi as math_pi, sqrt as math_sqrt, acos as math_acos, sin as math_sin

def process_test_case():
    epsilon_main = 1e-9
    width_val, height_val, area_a_val, area_b_val, target_c_val = map(int, input_read().split())
    if width_val == 0:
        return False

    radius_a = math_sqrt(area_a_val / math_pi)
    radius_b = math_sqrt(area_b_val / math_pi)
    radius_max = max(radius_a, radius_b)
    if 2 * radius_max > min(width_val, height_val) - epsilon_main:
        output_write("impossible\n")
        return True

    def compute_min_distance(r1, r2, area_target):
        epsilon_sub = 1e-8
        dist_lower = abs(r1 - r2) + epsilon_sub
        dist_upper = r1 + r2 - epsilon_sub
        while dist_lower + epsilon_sub < dist_upper:
            dist_mid = (dist_lower + dist_upper) / 2
            angle_1 = math_acos((r1 ** 2 + dist_mid ** 2 - r2 ** 2) / (2 * r1 * dist_mid))
            angle_2 = math_acos((r2 ** 2 + dist_mid ** 2 - r1 ** 2) / (2 * r2 * dist_mid))
            sector_area = ((2 * angle_1 - math_sin(2 * angle_1)) * r1 ** 2 + (2 * angle_2 - math_sin(2 * angle_2)) * r2 ** 2) / 2
            if sector_area < area_target:
                dist_upper = dist_mid
            else:
                dist_lower = dist_mid
        return dist_upper

    min_distance = compute_min_distance(radius_a, radius_b, target_c_val)
    direct_distance = abs(radius_a - radius_b)
    if direct_distance - epsilon_main < min_distance:
        x_gap = width_val - radius_a - radius_b
        y_gap = height_val - radius_a - radius_b
        diagonal_dist = math_sqrt(x_gap ** 2 + y_gap ** 2)
        pos_a_x = pos_a_y = radius_a
        pos_b_x = radius_a + x_gap * min_distance / diagonal_dist
        pos_b_y = radius_a + y_gap * min_distance / diagonal_dist
        if pos_b_x - radius_b < 0:
            pos_a_x -= pos_b_x - radius_b
            pos_b_x = radius_b
        if pos_b_y - radius_b < 0:
            pos_a_y -= pos_b_y - radius_b
            pos_b_y = radius_b
        if min_distance < diagonal_dist:
            output_write("%.16f %.16f %.16f %.16f %.16f %.16f\n" % (pos_a_x, pos_a_y, radius_a, pos_b_x, pos_b_y, radius_b))
        else:
            output_write("impossible\n")
    else:
        output_write("%.16f %.16f %.16f %.16f %.16f %.16f\n" % (radius_max, radius_max, radius_a, radius_max, radius_max, radius_b))
    return True

while process_test_case():
    pass