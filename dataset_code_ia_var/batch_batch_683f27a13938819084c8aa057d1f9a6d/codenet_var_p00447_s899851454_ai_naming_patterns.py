def process_case(line_count):
    source_list = sorted([list(map(int, input().split())) for _ in [0] * int(line_count)], key=lambda pair: pair[0])
    target_list = sorted([list(map(int, input().split())) for _ in [0] * int(input())], key=lambda pair: pair[0])
    for target_x, target_y in target_list:
        source_x, source_y = source_list[0]
        delta_x = target_x - source_x
        delta_y = target_y - source_y
        for src_x, src_y in source_list:
            mapped_point = [src_x + delta_x, src_y + delta_y]
            if mapped_point not in target_list:
                break
        else:
            print(delta_x, delta_y)
            return
for case_line_count in iter(input, '0'):
    process_case(case_line_count)