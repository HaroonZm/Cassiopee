test_case_count = int(input())
for test_case_index in range(test_case_count):
    block_count = int(input())
    block_list = list(map(int, input().split()))
    max_diff_forward = 0
    max_diff_backward = 0
    for block_index in range(1, block_count):
        diff_forward = block_list[block_index] - block_list[block_index - 1]
        diff_backward = block_list[block_index - 1] - block_list[block_index]
        max_diff_forward = max(max_diff_forward, diff_forward)
        max_diff_backward = max(max_diff_backward, diff_backward)
    print(max_diff_forward, max_diff_backward)