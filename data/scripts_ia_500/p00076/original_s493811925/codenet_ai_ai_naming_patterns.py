import sys
for input_line in sys.stdin:
    if input_line == '-1\n':
        break
    steps = int(input_line) - 1
    current_position = 1
    for _ in range(steps):
        direction = current_position * 1j
        normalized_direction = direction / abs(direction)
        current_position += normalized_direction
    print(current_position.real)
    print(current_position.imag)