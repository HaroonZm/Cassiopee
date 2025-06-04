from itertools import accumulate
input_count = int(input())
range_marks = [0] * 100002
for _ in range(input_count):
    range_start, range_end = map(int, input().split())
    range_marks[range_start - 1] += 1
    range_marks[range_end] -= 1
coverage_counts = list(accumulate(range_marks))
for candidate_value in range(input_count, -1, -1):
    if candidate_value <= coverage_counts[candidate_value]:
        print(candidate_value)
        break