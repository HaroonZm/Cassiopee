import math

while True:

    base_value, exponent_value = map(int, input().split())

    if base_value == 0 and exponent_value == 0:
        break

    power_result = pow(base_value, exponent_value)

    segmented_powers_of_ten = [
        68, 64, 60, 56, 52, 48, 44, 40, 36,
        32, 28, 24, 20, 16, 12, 8, 4, 0
    ]

    power_segments = []

    remaining_value = power_result

    for power_of_ten in segmented_powers_of_ten[:-1]:
        current_segment = remaining_value // pow(10, power_of_ten)
        power_segments.append(current_segment)
        remaining_value = remaining_value % pow(10, power_of_ten)

    # Append the last remaining segment (for the last 4 digits)
    power_segments.append(remaining_value)

    japanese_number_units = [
        'Mts', 'Fks', 'Nyt', 'Asg', 'Ggs', 'Gok', 'Sai', 'Sei',
        'Kan', 'Ko', 'Jou', 'Jo', 'Gai', 'Kei', 'Cho', 'Oku', 'Man', ''
    ]

    for index in range(len(power_segments)):
        current_segment_value = power_segments[index]
        if current_segment_value == 0:
            continue
        else:
            print(current_segment_value, end='')
            print(japanese_number_units[index], end='')

    print('')