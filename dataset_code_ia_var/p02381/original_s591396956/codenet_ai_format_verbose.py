import math

while True:
    number_of_elements = int(input())

    if number_of_elements == 0:
        break

    elements_list = [int(element) for element in input().split()]

    average_value = sum(elements_list) / number_of_elements

    squared_differences_sum = 0

    for index in range(number_of_elements):
        squared_differences_sum += (elements_list[index] - average_value) ** 2

    variance = squared_differences_sum / number_of_elements

    standard_deviation = math.sqrt(variance)

    print(standard_deviation)