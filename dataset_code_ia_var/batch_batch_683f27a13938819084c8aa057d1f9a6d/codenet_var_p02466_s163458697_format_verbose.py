def main():

    number_of_integers_first_set = int(input())

    integers_first_set = set(
        [int(integer_str) for integer_str in input().split()]
    )

    number_of_integers_second_set = int(input())

    integers_second_set = set(
        [int(integer_str) for integer_str in input().split()]
    )

    symmetric_difference_set = integers_first_set.symmetric_difference(
        integers_second_set
    )

    sorted_symmetric_difference_list = sorted(symmetric_difference_set)

    for value in sorted_symmetric_difference_list:
        print(value)

main()