MODULO_DIVISOR = 1000000007
EPSILON = 10 ** -9

def main():
    import sys

    input_function = sys.stdin.readline

    number_of_terms, max_height, difference_limit = map(int, input_function().split())

    range_difference_array = [0] * (max_height + 2)
    accumulated_answers = [0] * (max_height + 1)

    factorial_modulo = 1
    factorial_sum_modulo = 0

    # Calculer la factorielle et sa somme modulo MODULO_DIVISOR pour N éléments
    for current_number in range(1, number_of_terms + 1):
        factorial_modulo = (factorial_modulo * current_number) % MODULO_DIVISOR
        factorial_sum_modulo = (factorial_sum_modulo + factorial_modulo) % MODULO_DIVISOR

    # Application initiale de la méthode IMOS (table des différences)
    range_difference_array[1] += factorial_modulo
    range_difference_array[difference_limit + 1] -= factorial_modulo

    # Propagation des valeurs pour chaque hauteur jusqu'à max_height
    for current_height in range(1, max_height):

        accumulated_answers[current_height] = (
            accumulated_answers[current_height - 1] + range_difference_array[current_height]
        ) % MODULO_DIVISOR

        propagation_value = (accumulated_answers[current_height] * factorial_sum_modulo) % MODULO_DIVISOR

        range_difference_array[current_height + 1] = (
            range_difference_array[current_height + 1] + propagation_value
        ) % MODULO_DIVISOR

        if current_height + difference_limit + 1 <= max_height:
            range_difference_array[current_height + difference_limit + 1] = (
                range_difference_array[current_height + difference_limit + 1] - propagation_value
            ) % MODULO_DIVISOR

    print((accumulated_answers[max_height - 1] + range_difference_array[max_height]) % MODULO_DIVISOR)

if __name__ == '__main__':
    main()