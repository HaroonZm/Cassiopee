begin_index, end_index = map(int, input().split())
coverage_array = [0] * 1000
number_of_intervals = int(input())
for _ in range(number_of_intervals):
    interval_start, interval_end = map(int, input().split())
    for position in range(interval_start, interval_end):
        coverage_array[position] = 1

def is_covered():
    for position in range(begin_index, end_index):
        if coverage_array[position] == 1:
            return 1
    return 0

print(is_covered())