def calculate_greatest_common_divisor(first_integer: int, second_integer: int) -> int:
    if second_integer == 0:
        return first_integer

    return calculate_greatest_common_divisor(second_integer, first_integer % second_integer)


def main():
    while True:
        try:
            user_input_list = list(map(int, input().split()))

            first_value = user_input_list[0]
            second_value = user_input_list[1]

            greatest_common_divisor = calculate_greatest_common_divisor(first_value, second_value)
            least_common_multiple = int(first_value / greatest_common_divisor * second_value)

            print('%s %d' % (greatest_common_divisor, least_common_multiple))
        except:
            break


if __name__ == "__main__":
    main()