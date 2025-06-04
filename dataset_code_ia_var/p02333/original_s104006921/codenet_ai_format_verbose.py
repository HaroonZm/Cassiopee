from math import factorial

def read_two_integers_from_input():
    return map(int, input().rstrip().split())

def main():
    total_elements, group_count = read_two_integers_from_input()
    modulo = 10**9 + 7

    if total_elements < group_count:
        print(0)
        return

    if total_elements == group_count:
        print(factorial(total_elements) % modulo)
        return

    total_arrangements = 0
    binomial_coefficient = 1

    for inclusion_exclusion_index in range(group_count):
        sign = (-1) ** inclusion_exclusion_index
        current_term = sign * binomial_coefficient * pow(group_count - inclusion_exclusion_index, total_elements, modulo)
        total_arrangements = (total_arrangements + current_term) % modulo
        binomial_coefficient = binomial_coefficient * (group_count - inclusion_exclusion_index) // (inclusion_exclusion_index + 1)

    print(total_arrangements)

if __name__ == "__main__":
    main()