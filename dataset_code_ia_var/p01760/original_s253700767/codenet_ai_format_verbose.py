import sys

target_average_temperature, total_quantity = [int(value) for value in sys.stdin.readline().split()]

source_temperatures = [int(value) for value in sys.stdin.readline().split()]
source_quantities = [int(value) for value in sys.stdin.readline().split()]

minimum_temperature_difference = float("inf")

for first_source_units in range(total_quantity + 1):

    first_source_quantity = source_quantities[0] * first_source_units

    if first_source_quantity > total_quantity:
        continue

    for second_source_units in range(total_quantity + 1):

        second_source_quantity = source_quantities[1] * second_source_units

        total_mixture_quantity = first_source_quantity + second_source_quantity

        if total_mixture_quantity > total_quantity or total_mixture_quantity < 1:
            continue

        total_mixture_temperature = (first_source_quantity * source_temperatures[0]) + \
                                   (second_source_quantity * source_temperatures[1])

        average_mixture_temperature = total_mixture_temperature / total_mixture_quantity

        temperature_difference = abs(target_average_temperature - average_mixture_temperature)

        if temperature_difference < minimum_temperature_difference:
            minimum_temperature_difference = temperature_difference

print(minimum_temperature_difference)