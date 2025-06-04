number_of_rows, number_of_height_units, number_of_width_units = map(int, input().split())

row_shifts = list(map(int, input().split()))

total_width_units = number_of_rows * number_of_width_units

coverage_flags_for_width_units = [False] * total_width_units

for row_index in range(number_of_rows):

    if (row_index + 1) % 2 == 1:  # Odd-indexed row (1-based)
        coverage_start = row_index * number_of_width_units + row_shifts[row_index]
        coverage_end = coverage_start + number_of_width_units
        for unit_index in range(coverage_start, coverage_end):
            coverage_flags_for_width_units[unit_index] = True

    else:  # Even-indexed row (1-based)
        coverage_start = row_index * number_of_width_units - row_shifts[row_index]
        coverage_end = coverage_start + number_of_width_units
        for unit_index in range(coverage_start, coverage_end):
            coverage_flags_for_width_units[unit_index] = True

number_of_uncovered_width_units = 0

for width_unit_covered in coverage_flags_for_width_units:
    if width_unit_covered is False:
        number_of_uncovered_width_units += 1

total_uncovered_tiles = number_of_uncovered_width_units * number_of_height_units

print(total_uncovered_tiles)