import sys
from sys import stdin

def read_input():
    return stdin.readline()

def main():
    num_elements = int(read_input())
    prefix_count_j = [0] * (num_elements + 1)
    prefix_count_i = [0] * (num_elements + 1)
    input_string = read_input().strip()

    for idx in range(num_elements):
        prefix_count_j[idx + 1] = prefix_count_j[idx] + (input_string[idx] == 'J')
        prefix_count_i[idx + 1] = prefix_count_i[idx] + (input_string[idx] == 'I')

    result_total = 0
    max_product_j_before_i_after = 0
    sum_i_after_o = 0
    sum_j_before_o = 0
    cross_product_o = 0

    for idx in range(1, num_elements):
        max_product_j_before_i_after = max(
            max_product_j_before_i_after, 
            prefix_count_j[idx] * (prefix_count_i[num_elements] - prefix_count_i[idx])
        )

    for idx in range(num_elements):
        if input_string[idx] == 'O':
            sum_i_after_o += prefix_count_i[num_elements] - prefix_count_i[idx + 1]
            sum_j_before_o += prefix_count_j[idx]
            cross_product_o += (prefix_count_i[num_elements] - prefix_count_i[idx + 1]) * prefix_count_j[idx]

    result_total = cross_product_o + max(max_product_j_before_i_after, sum_i_after_o, sum_j_before_o)
    print(result_total)

if __name__ == '__main__':
    main()