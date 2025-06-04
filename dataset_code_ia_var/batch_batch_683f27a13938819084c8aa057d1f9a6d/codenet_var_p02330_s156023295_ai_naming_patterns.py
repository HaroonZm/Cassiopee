import sys
import bisect

def read_int_list(): return [int(token) for token in sys.stdin.readline().split()]
def read_single_int(): return int(sys.stdin.readline())
def read_char_lists(): return [list(token) for token in sys.stdin.readline().split()]
def read_char_line():
    result = list(sys.stdin.readline())
    if result and result[-1] == "\n":
        return result[:-1]
    return result
def read_int_lines(num_lines): return [read_single_int() for _ in range(num_lines)]
def read_int_list_lines(num_lines): return [read_int_list() for _ in range(num_lines)]
def read_char_lines(num_lines): return [read_char_line() for _ in range(num_lines)]
def read_char_list_lines(num_lines): return [read_char_lists() for _ in range(num_lines)]

sys.setrecursionlimit(1000000)
MOD_CONST = 10**9 + 7

def main_solve():
    total_elements, select_count, lower_limit, upper_limit = read_int_list()
    element_list = read_int_list()
    left_size = total_elements // 2
    right_size = total_elements - left_size
    left_sum_partitions = [[] for _ in range(left_size + 1)]
    right_sum_partitions = [[] for _ in range(right_size + 1)]
    for left_mask in range(1 << left_size):
        left_sum = 0
        left_count = 0
        for idx in range(left_size):
            if left_mask & (1 << idx):
                left_sum += element_list[idx]
                left_count += 1
        left_sum_partitions[left_count].append(left_sum)
    for right_mask in range(1 << right_size):
        right_sum = 0
        right_count = 0
        for idx in range(right_size):
            if right_mask & (1 << idx):
                right_sum += element_list[idx + left_size]
                right_count += 1
        right_sum_partitions[right_count].append(right_sum)
    for size in range(right_size + 1):
        right_sum_partitions[size].sort()
    total_options = 0
    for left_count in range(left_size + 1):
        if left_count > select_count:
            break
        right_count = select_count - left_count
        if right_count > right_size:
            continue
        for left_partial_sum in left_sum_partitions[left_count]:
            lower_bound = bisect.bisect_left(right_sum_partitions[right_count], lower_limit - left_partial_sum)
            upper_bound = bisect.bisect_right(right_sum_partitions[right_count], upper_limit - left_partial_sum)
            total_options += upper_bound - lower_bound
    print(total_options)

if __name__ == "__main__":
    main_solve()