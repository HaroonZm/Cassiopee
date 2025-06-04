import math

# Lecture de la ligne d'entrée
input_line = input()

# Séparation de la ligne en éléments individuels
input_values = input_line.split()

# Extraction des deux entiers depuis la liste d'entrée
number_of_items = int(input_values[0])
number_of_boxes = int(input_values[1])

def calculate_number_of_combinations(total_elements, elements_to_choose):
    numerator = math.factorial(total_elements)
    denominator = math.factorial(total_elements - elements_to_choose) * math.factorial(elements_to_choose)
    return numerator // denominator

modulo_value = 10 ** 9 + 7

number_of_ways = calculate_number_of_combinations(number_of_items + number_of_boxes - 1, number_of_items)

result = number_of_ways % modulo_value

print(result)