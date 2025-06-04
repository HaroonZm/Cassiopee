def compute_result(height_input, width_input):
    area_square_sum = height_input * height_input + width_input * width_input
    result_candidates = []
    for candidate_x in range(1, 151):
        for candidate_y in range(candidate_x + 1, 151):
            candidate_square_sum = candidate_x ** 2 + candidate_y ** 2
            if area_square_sum <= candidate_square_sum:
                result_candidates.append((candidate_square_sum, candidate_x, candidate_y))
    result_candidates.sort()
    for candidate_square_sum, candidate_x, candidate_y in result_candidates:
        if area_square_sum < candidate_square_sum or candidate_x > height_input:
            final_result = [candidate_x, candidate_y]
            break
    print(" ".join(map(str, final_result)))

while True:
    input_height, input_width = map(int, input().split())
    if input_height == 0 and input_width == 0:
        break
    compute_result(input_height, input_width)