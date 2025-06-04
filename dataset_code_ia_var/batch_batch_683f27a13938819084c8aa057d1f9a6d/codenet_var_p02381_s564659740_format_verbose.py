number_of_elements = int(input())

while number_of_elements != 0:

    input_values = [int(value) for value in input().split()]

    mean_of_values = sum(input_values) / number_of_elements

    sum_of_squared_differences = 0

    for index in range(number_of_elements):

        squared_difference = (input_values[index] - mean_of_values) ** 2

        sum_of_squared_differences += squared_difference

    standard_deviation = (sum_of_squared_differences / number_of_elements) ** 0.5

    print(standard_deviation)

    number_of_elements = int(input())