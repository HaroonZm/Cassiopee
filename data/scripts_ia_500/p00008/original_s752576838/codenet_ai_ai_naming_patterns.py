from collections import deque
import sys

def compute_solution(sequence_length, target_sum):
    if sequence_length <= 1:
        if 0 <= target_sum <= 9:
            sequence_queue.append(target_sum)
            return target_sum
        else:
            return None
    else:
        for digit in range(10):
            compute_solution(sequence_length - 1, target_sum - digit)

sequence_queue = deque()

if __name__ == '__main__':
    for input_line in sys.stdin:
        current_target = int(input_line)
        compute_solution(4, current_target)
        print(len(sequence_queue))
        sequence_queue.clear()