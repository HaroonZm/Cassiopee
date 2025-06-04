MAXIMUM_NUMBER_LIMIT = 1000004

initial_prime_list = [
    3,   5,   7,  11,  13,  17,  19,  23,  29,
    31,  37,  41,  43,  47,  53,  59,  61,  67,  71,
    73,  79,  83,  89,  97, 101, 103, 107, 109, 113,
    127, 131, 137, 139, 149, 151, 157, 163, 167, 173,
    179, 181, 191, 193, 197, 199, 211, 223, 227, 229,
    233, 239, 241, 251, 257, 263, 269, 271, 277, 281,
    283, 293, 307, 311, 313, 317, 331, 337, 347, 349,
    353, 359, 367, 373, 379, 383, 389, 397, 401, 409,
    419, 421, 431, 433, 439, 443, 449, 457, 461, 463,
    467, 479, 487, 491, 499, 503, 509, 521, 523, 541,
    547, 557, 563, 569, 571, 577, 587, 593, 599, 601,
    607, 613, 617, 619, 631, 641, 643, 647, 653, 659,
    661, 673, 677, 683, 691, 701, 709, 719, 727, 733,
    739, 743, 751, 757, 761, 769, 773, 787, 797, 809,
    811, 821, 823, 827, 829, 839, 853, 857, 859, 863,
    877, 881, 883, 887, 907, 911, 919, 929, 937, 941,
    947, 953, 967, 971, 977, 983, 991, 997
]

def generate_composite_table():
    for prime_number in initial_prime_list:
        for multiple in range(prime_number * prime_number, MAXIMUM_NUMBER_LIMIT, prime_number):
            is_composite_table[multiple] = 1

    for odd_candidate in range(997, MAXIMUM_NUMBER_LIMIT, 2):
        if is_composite_table[odd_candidate] == 0:
            initial_prime_list.append(odd_candidate)

def calculate_prime_factor_exponents(number):
    prime_exponent_list = []

    if (number & 1) == 0:
        factor_exponent_count = 0
        while True:
            number >>= 1
            factor_exponent_count += 1
            if number & 1:
                break
        prime_exponent_list.append(factor_exponent_count)

    if number <= 1:
        return prime_exponent_list

    if number <= MAXIMUM_NUMBER_LIMIT and is_composite_table[number] == 0:
        prime_exponent_list.append(1)
        return prime_exponent_list

    sqrt_number = int(number ** 0.5)

    for prime_candidate in initial_prime_list:
        if number <= 1:
            break

        if prime_candidate > sqrt_number or (number <= MAXIMUM_NUMBER_LIMIT and is_composite_table[number] == 0):
            prime_exponent_list.append(1)
            break

        if number % prime_candidate:
            continue

        factor_exponent_count = 0
        while True:
            number //= prime_candidate
            factor_exponent_count += 1
            if number % prime_candidate:
                break
        prime_exponent_list.append(factor_exponent_count)

    return prime_exponent_list

is_composite_table = [0] * MAXIMUM_NUMBER_LIMIT

generate_composite_table()

while True:
    user_input_number = int(input())

    if user_input_number == 0:
        break

    if user_input_number == 1:
        print(1)
        continue

    if (user_input_number <= MAXIMUM_NUMBER_LIMIT and (user_input_number & 1) and is_composite_table[user_input_number] == 0):
        print(2)
        continue

    prime_exponent_list = calculate_prime_factor_exponents(user_input_number)

    divisors_count = 1
    for exponent_value in prime_exponent_list:
        divisors_count *= (1 + (exponent_value << 1))

    print((divisors_count + 1) >> 1)