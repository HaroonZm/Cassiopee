test_case_count = int(input())
for test_case_index in range(test_case_count):
    element_count = int(input())
    element_list = list(map(int, input().split()))
    max_difference = 0
    min_difference = 0
    for difference_index in range(element_count - 1):
        current_difference = element_list[difference_index + 1] - element_list[difference_index]
        max_difference = max(current_difference, max_difference)
        min_difference = min(current_difference, min_difference)
    print(max_difference, -min_difference)