def main():

    number_of_elements_to_read = input()

    list_of_integers = list(map(int, input().split()))

    sorted_list_of_integers = sorted(list_of_integers)

    length_of_list = len(sorted_list_of_integers)

    middle_index = length_of_list // 2

    value_at_middle_index = sorted_list_of_integers[middle_index]
    value_before_middle_index = sorted_list_of_integers[middle_index - 1]

    difference_between_middle_elements = value_at_middle_index - value_before_middle_index

    print(difference_between_middle_elements)


if __name__ == '__main__':
    main()