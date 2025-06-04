def main():
    total_number_of_elements = input()
    integer_sequence = [int(element) for element in input().split(" ")]
    number_of_queries = int(input())

    for query_index in range(number_of_queries):

        range_start_index, range_end_index = map(int, input().split(" "))

        sub_sequence_to_reverse = integer_sequence[range_start_index:range_end_index]

        reversed_sub_sequence = sub_sequence_to_reverse[::-1]

        integer_sequence[range_start_index:range_end_index] = reversed_sub_sequence[:]

    print(*integer_sequence)

main()