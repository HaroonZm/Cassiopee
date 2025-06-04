from math import gcd

def calculate_modular_sum_of_lcms():
    number_count = int(input())

    list_of_numbers = list(map(int, input().split()))

    modulo_value = 10**9 + 7

    total_sum = 0

    least_common_multiple = 1

    for current_number in list_of_numbers:
        least_common_multiple = least_common_multiple * current_number // gcd(least_common_multiple, current_number)

    least_common_multiple = least_common_multiple % modulo_value

    for current_number in list_of_numbers:
        modular_inverse = pow(current_number, modulo_value - 2, modulo_value)
        total_sum += least_common_multiple * modular_inverse

    result = total_sum % modulo_value

    print(result)

if __name__ == "__main__":

    calculate_modular_sum_of_lcms()