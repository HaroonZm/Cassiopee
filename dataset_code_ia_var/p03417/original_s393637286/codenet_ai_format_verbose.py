number_of_rows, number_of_columns = map(int, input().split())

if number_of_rows == 1 and number_of_columns == 1:
    print(1)

elif number_of_rows == 1:
    print(number_of_columns - 2)

elif number_of_columns == 1:
    print(number_of_rows - 2)

else:
    print((number_of_rows - 2) * (number_of_columns - 2))