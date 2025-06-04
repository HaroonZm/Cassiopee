import sys
from collections import Counter

sys.setrecursionlimit(1000000)

def main_process():
    input_value_count, input_value_number = (int(element) for element in input().split())
    result_accumulator = 1
    if input_value_count == 1:
        print(input_value_number)
        exit()
    processing_number = input_value_number
    for divisor_candidate in range(2, int(processing_number ** 0.5) + 4):
        divisor_count = 0
        while processing_number % divisor_candidate == 0:
            divisor_count += 1
            processing_number //= divisor_candidate
            if divisor_count >= input_value_count:
                result_accumulator *= divisor_candidate
                divisor_count -= input_value_count
    print(result_accumulator)

main_process()