amida_lines = []

def amida_main():
    vertical_line_count = int(raw_input())
    wire_line_count = int(raw_input())

    amida_initialize(vertical_line_count)

    processed_wire_lines = 0
    while processed_wire_lines < wire_line_count:
        wire_line_positions = raw_input().strip().split(',')
        amida_transpose(int(wire_line_positions[0]), int(wire_line_positions[1]))
        processed_wire_lines += 1

    for vertical_line_index in range(1, vertical_line_count + 1):
        print amida_lines[vertical_line_index]

def amida_initialize(vertical_line_count):
    for vertical_line_index in range(vertical_line_count + 1):
        amida_lines.append(vertical_line_index)

def amida_transpose(position_a, position_b):
    temp_value = amida_lines[position_a]
    amida_lines[position_a] = amida_lines[position_b]
    amida_lines[position_b] = temp_value

amida_main()