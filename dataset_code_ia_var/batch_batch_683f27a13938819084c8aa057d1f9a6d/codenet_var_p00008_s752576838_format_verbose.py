from collections import deque
import sys

def find_combinations(number_of_digits, required_sum):
    """
    Recursive function that finds all combinations of a given number of digits (0-9)
    which sum to required_sum. Valid combinations are appended to the global results_queue.
    """
    if number_of_digits <= 1:
        if 0 <= required_sum <= 9:
            results_queue.append(required_sum)
            return required_sum
        else:
            return None
    else:
        for digit in range(10):
            find_combinations(number_of_digits - 1, required_sum - digit)

results_queue = deque()

if __name__ == '__main__':
    
    for input_line in sys.stdin:
        
        required_sum = int(input_line)
        
        find_combinations(4, required_sum)
        
        total_valid_combinations = len(results_queue)
        print(total_valid_combinations)
        
        results_queue.clear()