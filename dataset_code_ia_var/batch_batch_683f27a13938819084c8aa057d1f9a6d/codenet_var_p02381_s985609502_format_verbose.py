import math

def read_list_of_integers_from_input_line():
    input_line = input().split()
    list_of_integers = []
    for element in input_line:
        list_of_integers.append(int(element))
    return list_of_integers

def main():
    while True:
        number_of_elements = int(input())
        if number_of_elements == 0:
            break

        data_values = read_list_of_integers_from_input_line()

        sum_of_values = 0
        sum_of_squares = 0

        for data_value in data_values:
            sum_of_values += data_value
            sum_of_squares += data_value ** 2

        mean_value = sum_of_values / number_of_elements
        mean_of_squares = sum_of_squares / number_of_elements

        standard_deviation = math.sqrt(mean_of_squares - (mean_value ** 2))

        print(standard_deviation)

if __name__ == "__main__":
    main()