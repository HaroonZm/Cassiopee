from statistics import pstdev

while True:

    user_exit_command = input()

    if user_exit_command == "0":
        break

    user_input_numbers = input()

    list_of_integers = [int(number_string) for number_string in user_input_numbers.split()]

    population_standard_deviation = pstdev(list_of_integers)

    print(population_standard_deviation)