def read_integers_from_input():
    return list(map(int, input().split()))

MODULUS = 10 ** 9 + 7

minimum_value, maximum_value, target_value = read_integers_from_input()

if target_value < minimum_value:
    print(target_value % MODULUS)
else:
    number_of_full_cycles = (target_value - maximum_value) // (minimum_value - maximum_value)
    result = (target_value + number_of_full_cycles * maximum_value) % MODULUS
    print(result)