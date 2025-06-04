import math

IDX_X = 0
IDX_Y = 1

POINT_START = (0.0, 0.0)
POINT_END = (100.0, 0.0)

ANGLE_DEGREES = 60
SIN_THETA = math.sin(math.radians(ANGLE_DEGREES))
COS_THETA = math.cos(math.radians(ANGLE_DEGREES))

input_depth = int(input())

def generate_koch_curve(recursion_depth, coord_a, coord_b):
    if recursion_depth == 0:
        return

    third_point = (
        (2.0 * coord_a[IDX_X] + 1.0 * coord_b[IDX_X]) / 3.0,
        (2.0 * coord_a[IDX_Y] + 1.0 * coord_b[IDX_Y]) / 3.0
    )
    two_third_point = (
        (1.0 * coord_a[IDX_X] + 2.0 * coord_b[IDX_X]) / 3.0,
        (1.0 * coord_a[IDX_Y] + 2.0 * coord_b[IDX_Y]) / 3.0
    )
    peak_point = (
        (two_third_point[IDX_X] - third_point[IDX_X]) * COS_THETA - (two_third_point[IDX_Y] - third_point[IDX_Y]) * SIN_THETA + third_point[IDX_X],
        (two_third_point[IDX_X] - third_point[IDX_X]) * SIN_THETA + (two_third_point[IDX_Y] - third_point[IDX_Y]) * COS_THETA + third_point[IDX_Y]
    )

    generate_koch_curve(recursion_depth - 1, coord_a, third_point)
    print("{:.8f} {:.8f}".format(third_point[IDX_X], third_point[IDX_Y]))
    generate_koch_curve(recursion_depth - 1, third_point, peak_point)
    print("{:.8f} {:.8f}".format(peak_point[IDX_X], peak_point[IDX_Y]))
    generate_koch_curve(recursion_depth - 1, peak_point, two_third_point)
    print("{:.8f} {:.8f}".format(two_third_point[IDX_X], two_third_point[IDX_Y]))
    generate_koch_curve(recursion_depth - 1, two_third_point, coord_b)

print("{:.8f} {:.8f}".format(POINT_START[IDX_X], POINT_START[IDX_Y]))
generate_koch_curve(input_depth, POINT_START, POINT_END)
print("{:.8f} {:.8f}".format(POINT_END[IDX_X], POINT_END[IDX_Y]))