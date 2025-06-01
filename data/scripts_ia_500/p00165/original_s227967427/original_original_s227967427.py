import bisect

LENGTH = 1000000

def eratosthenes(length):
    from math import sqrt

    def is_prime_number(num):
        limit = int(sqrt(num)) + 1

        for lp in range(3, limit, 2):
            if num % lp == 0:
                return False

        return True

    is_prime_number_list = [True] * (LENGTH + 1)
    is_prime_number_list[0] = False
    is_prime_number_list[1] = False
    is_prime_number_list[2] = True

    for index in range(4, length + 1, 2):
        is_prime_number_list[index] = False

    limit = int(sqrt(length)) + 1

    for lp in range(3, limit, 2):
        if is_prime_number(lp):

            for index in range(lp * 2, length + 1, lp):
                is_prime_number_list[index] = False

    return is_prime_number_list

is_prime_number_list = eratosthenes(LENGTH)
prime_number_list = [index for index, item in enumerate(is_prime_number_list) if item]

while True:
    input_count = int(input())

    if input_count == 0:
        break

    pay = 0

    for _ in range(input_count):
        p, m = [int(item) for item in input().split(" ")]

        lower = p - m if 0 < p - m else 0
        upper = p + m if p + m < LENGTH else LENGTH

        lower_index = bisect.bisect_left(prime_number_list, lower)
        upper_index = bisect.bisect_right(prime_number_list, upper)

        prize = upper_index - lower_index
        pay += prize - 1

    print(pay)