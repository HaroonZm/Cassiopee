import math

ANGLE_RADIANS = math.radians(60.0)

class Coordinate:
    def __init__(self, x_value, y_value):
        self.x_value = x_value
        self.y_value = y_value

def koch_curve_iteration(step_count, point_start, point_end):
    if step_count == 0:
        return
    point_s = Coordinate((2.0 * point_start.x_value + point_end.x_value) / 3.0,
                        (2.0 * point_start.y_value + point_end.y_value) / 3.0)
    point_t = Coordinate((point_start.x_value + 2.0 * point_end.x_value) / 3.0,
                        (point_start.y_value + 2.0 * point_end.y_value) / 3.0)
    u_x = (point_t.x_value - point_s.x_value) * math.cos(ANGLE_RADIANS) - (point_t.y_value - point_s.y_value) * math.sin(ANGLE_RADIANS) + point_s.x_value
    u_y = (point_t.x_value - point_s.x_value) * math.sin(ANGLE_RADIANS) + (point_t.y_value - point_s.y_value) * math.cos(ANGLE_RADIANS) + point_s.y_value
    point_u = Coordinate(u_x, u_y)

    koch_curve_iteration(step_count - 1, point_start, point_s)
    print(point_s.x_value, point_s.y_value)
    koch_curve_iteration(step_count - 1, point_s, point_u)
    print(point_u.x_value, point_u.y_value)
    koch_curve_iteration(step_count - 1, point_u, point_t)
    print(point_t.x_value, point_t.y_value)
    koch_curve_iteration(step_count - 1, point_t, point_end)

def main():
    recursion_depth = int(input())
    koch_point_start = Coordinate(0.0, 0.0)
    koch_point_end = Coordinate(100.0, 0.0)

    print(koch_point_start.x_value, koch_point_start.y_value)
    koch_curve_iteration(recursion_depth, koch_point_start, koch_point_end)
    print(koch_point_end.x_value, koch_point_end.y_value)

if __name__ == "__main__":
    main()