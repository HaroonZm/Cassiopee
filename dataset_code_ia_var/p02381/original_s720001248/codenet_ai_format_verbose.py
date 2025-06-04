while True:
    number_of_elements = int(input())
    
    if number_of_elements == 0:
        break

    input_numbers = [int(element) for element in input().split()]
    
    average_value = sum(input_numbers) / len(input_numbers)
    
    sum_squared_differences = 0
    
    for current_number in input_numbers:
        sum_squared_differences += (current_number - average_value) ** 2

    standard_deviation = (sum_squared_differences / len(input_numbers)) ** 0.5

    print(format(standard_deviation, '.6f'))