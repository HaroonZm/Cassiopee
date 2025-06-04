import math

def calculate_standard_deviation(list_of_numbers):

    number_of_elements = len(list_of_numbers)

    mean_of_elements = float(sum(list_of_numbers)) / number_of_elements

    sum_of_squared_differences = 0.0

    for current_number in list_of_numbers:

        difference_from_mean = current_number - mean_of_elements

        sum_of_squared_differences += difference_from_mean * difference_from_mean

    standard_deviation = math.sqrt(sum_of_squared_differences / number_of_elements)

    return standard_deviation

while True:

    user_input = raw_input()

    if user_input == "0":
        break

    number_string_list = raw_input().split(" ")

    number_list = map(float, number_string_list)

    standard_deviation_result = calculate_standard_deviation(number_list)

    print standard_deviation_result