number_of_rows, number_of_columns = [int(value) for value in input().split()]

def main():

    adjusted_rows = number_of_rows - 1
    adjusted_columns = number_of_columns - 1

    if adjusted_rows == 0 and adjusted_columns == 0:
        answer = 1

    elif adjusted_rows == 0 or adjusted_columns == 0:
        answer = adjusted_rows + adjusted_columns - 1

    else:
        answer = (adjusted_rows - 1) * (adjusted_columns - 1)

    print(answer)


if __name__ == "__main__":
    main()