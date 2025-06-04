def compute_min_diagonal_length(segment_a, segment_b, segment_c):
    segment_lengths = [segment_a, segment_b, segment_c]
    segment_lengths.sort()
    smallest_sum_of_squares = segment_lengths[0] ** 2 + segment_lengths[1] ** 2
    min_diagonal_length = smallest_sum_of_squares ** 0.5
    return min_diagonal_length

while True:
    input_segments = tuple(map(float, input().split()))
    if input_segments == (0, 0, 0):
        break
    num_radii = int(input())
    radius_list = [None] * num_radii
    for radius_index in range(num_radii):
        radius_list[radius_index] = float(input())
    minimal_diagonal = compute_min_diagonal_length(*input_segments)
    for radius_value in radius_list:
        if minimal_diagonal < 2 * radius_value:
            print("OK")
        else:
            print("NA")