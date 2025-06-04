input_range_count, input_forbidden_digits_count = map(int, input().split())
forbidden_digits_set = {int(forbidden_digit) for forbidden_digit in input().split()}
result_value = None
for candidate_number in range(input_range_count, input_range_count * 10):
    candidate_digits_set = {int(candidate_digit) for candidate_digit in str(candidate_number)}
    if forbidden_digits_set.isdisjoint(candidate_digits_set):
        result_value = candidate_number
        break
print(result_value)