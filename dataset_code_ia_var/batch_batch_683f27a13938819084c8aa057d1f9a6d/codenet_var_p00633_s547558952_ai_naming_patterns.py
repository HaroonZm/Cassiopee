def parse_string_to_float_list(input_string):
    return list(map(float, input_string.split()))

def process_circles():
    from sys import stdin
    import itertools
    import math
    import cmath
    import bisect

    input_lines = stdin.readlines()
    while True:
        total_circles = int(input_lines[0])
        if total_circles == 0:
            break

        circle_data_list = list(map(parse_string_to_float_list, input_lines[1:1+total_circles]))
        circle_indexed_data = list(enumerate(circle_data_list))
        merge_angle_events = [[] for _ in range(total_circles)]
        circle_included_flags = [False] * total_circles
        total_radius_sum = sum(circle_data[2] for circle_data in circle_data_list)
        total_perimeter = 2 * math.pi * total_radius_sum

        for (index_a, data_a), (index_b, data_b) in itertools.combinations(circle_indexed_data, 2):
            if circle_included_flags[index_a] or circle_included_flags[index_b]:
                continue

            x_a, y_a, r_a = data_a
            x_b, y_b, r_b = data_b
            center_a = complex(x_a, y_a)
            center_b = complex(x_b, y_b)
            centers_vector = center_b - center_a
            centers_distance = abs(centers_vector)

            if centers_distance >= r_a + r_b:
                continue
            elif centers_distance <= abs(r_a - r_b):
                if r_a < r_b:
                    total_perimeter -= 2 * math.pi * r_a
                    circle_included_flags[index_a] = True
                else:
                    total_perimeter -= 2 * math.pi * r_b
                    circle_included_flags[index_b] = True
                continue

            angle_a = math.acos((r_a**2 + centers_distance**2 - r_b**2) / (2 * r_a * centers_distance))
            vector_angle_a = cmath.phase(centers_vector)
            arc_start_a = vector_angle_a - angle_a
            arc_end_a = vector_angle_a + angle_a
            arc_events_a = merge_angle_events[index_a]
            if arc_start_a >= -math.pi and arc_end_a <= math.pi:
                bisect.insort(arc_events_a, (arc_start_a, -1))
                bisect.insort(arc_events_a, (arc_end_a, 1))
            elif arc_start_a < -math.pi:
                bisect.insort(arc_events_a, (arc_start_a + 2 * math.pi, -1))
                bisect.insort(arc_events_a, (math.pi, 1))
                bisect.insort(arc_events_a, (-math.pi, -1))
                bisect.insort(arc_events_a, (arc_end_a, 1))
            else:
                bisect.insort(arc_events_a, (arc_start_a, -1))
                bisect.insort(arc_events_a, (math.pi, 1))
                bisect.insort(arc_events_a, (-math.pi, -1))
                bisect.insort(arc_events_a, (arc_end_a - 2 * math.pi, 1))

            angle_b = math.acos((r_b**2 + centers_distance**2 - r_a**2) / (2 * r_b * centers_distance))
            vector_angle_b = cmath.phase(-centers_vector)
            arc_start_b = vector_angle_b - angle_b
            arc_end_b = vector_angle_b + angle_b
            arc_events_b = merge_angle_events[index_b]
            if arc_start_b >= -math.pi and arc_end_b <= math.pi:
                bisect.insort(arc_events_b, (arc_start_b, -1))
                bisect.insort(arc_events_b, (arc_end_b, 1))
            elif arc_start_b < -math.pi:
                bisect.insort(arc_events_b, (arc_start_b + 2 * math.pi, -1))
                bisect.insort(arc_events_b, (math.pi, 1))
                bisect.insort(arc_events_b, (-math.pi, -1))
                bisect.insort(arc_events_b, (arc_end_b, 1))
            else:
                bisect.insort(arc_events_b, (arc_start_b, -1))
                bisect.insort(arc_events_b, (math.pi, 1))
                bisect.insort(arc_events_b, (-math.pi, -1))
                bisect.insort(arc_events_b, (arc_end_b - 2 * math.pi, 1))

        circle_radius_list = [circle_data[2] for circle_data in circle_data_list]
        for arc_event_list, current_radius in zip(merge_angle_events, circle_radius_list):
            event_state = 0
            for event_angle, event_flag in arc_event_list:
                if event_state == 0:
                    segment_start_angle = event_angle
                event_state += event_flag
                if event_state == 0:
                    total_perimeter -= current_radius * (event_angle - segment_start_angle)

        print(total_perimeter)

        del input_lines[:1+total_circles]

process_circles()