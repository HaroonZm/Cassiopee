from itertools import accumulate

def main():

    number_of_elements = int(input())

    numbers_list = list(map(int, input().split()))

    prefix_sums = [0] + list(accumulate(numbers_list))

    VERY_LARGE_NUMBER = 10 ** 10

    dynamic_programming_table = [[None] * number_of_elements for _ in range(number_of_elements)]

    for single_index in range(number_of_elements):
        dynamic_programming_table[single_index][single_index] = 0

    for current_length_of_subarray in range(2, number_of_elements + 1):

        for left_index in range(number_of_elements - current_length_of_subarray + 1):

            right_index = left_index + current_length_of_subarray - 1

            minimum_score_for_current_subarray = VERY_LARGE_NUMBER

            prefix_sum_to_right = prefix_sums[right_index + 1]
            prefix_sum_to_left = prefix_sums[left_index]

            for partition_point in range(left_index, right_index):

                left_partition_sum = prefix_sums[partition_point + 1] - prefix_sum_to_left
                right_partition_sum = prefix_sum_to_right - prefix_sums[partition_point + 1]

                split_score = dynamic_programming_table[left_index][partition_point] + dynamic_programming_table[partition_point + 1][right_index]

                carry_over = 0

                left_part_temp = left_partition_sum
                right_part_temp = right_partition_sum

                while left_part_temp or right_part_temp or carry_over:

                    left_digit = left_part_temp % 10
                    right_digit = right_part_temp % 10

                    split_score += left_digit * right_digit + carry_over

                    if minimum_score_for_current_subarray <= split_score:
                        break

                    carry_over = 0 if left_digit + right_digit + carry_over < 10 else 1

                    left_part_temp //= 10
                    right_part_temp //= 10

                else:
                    minimum_score_for_current_subarray = split_score

            dynamic_programming_table[left_index][right_index] = minimum_score_for_current_subarray

    print(dynamic_programming_table[0][number_of_elements - 1])

main()