def main():
    
    MODULUS = 1000000007

    first_string = input()
    second_string = input()

    length_first_string = len(first_string)
    length_second_string = len(second_string)

    dp_table = [[0 for column_index in range(length_second_string + 1)] for row_index in range(length_first_string + 1)]
    dp_table[0][0] = 1

    for index_first in range(length_first_string):

        for index_second in range(length_second_string - 1, -1, -1):

            dp_table[index_first + 1][index_second] += dp_table[index_first][index_second]
            dp_table[index_first + 1][index_second] %= MODULUS

            if first_string[index_first] == second_string[index_second]:
                dp_table[index_first + 1][index_second + 1] += dp_table[index_first][index_second]
                dp_table[index_first + 1][index_second + 1] %= MODULUS

    total_count = 0
    for row in range(length_first_string + 1):
        total_count += dp_table[row][length_second_string]

    print(total_count % MODULUS)


if __name__ == "__main__":
    main()