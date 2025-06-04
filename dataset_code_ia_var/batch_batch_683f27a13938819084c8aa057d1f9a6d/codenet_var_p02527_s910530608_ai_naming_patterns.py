#!/usr/bin/env python

def process_input_and_sort_numbers():
    input_count = raw_input()
    input_numbers_str = raw_input()
    input_numbers_list = [int(input_number_str) for input_number_str in input_numbers_str.split(" ")]
    input_numbers_list.sort()
    sorted_numbers_str_list = [str(sorted_number) for sorted_number in input_numbers_list]
    sorted_numbers_str = " ".join(sorted_numbers_str_list)
    print sorted_numbers_str

if __name__ == '__main__':
    process_input_and_sort_numbers()