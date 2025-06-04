def calc_factorials_and_inverses(max_n, modulus):
    factorial_list = [1] * (max_n + 1)
    inverse_list = [1] * (max_n + 1)
    current_factorial = 1
    for idx in range(1, max_n + 1):
        current_factorial = (current_factorial * idx) % modulus
        factorial_list[idx] = current_factorial
    inverse_list[max_n] = pow(factorial_list[max_n], modulus - 2, modulus)
    for idx in range(max_n - 1, -1, -1):
        inverse_list[idx] = (inverse_list[idx + 1] * (idx + 1)) % modulus
    return factorial_list, inverse_list

def calc_combination(n_value, r_value, modulus, factorial_list, inverse_list):
    if r_value < 0 or n_value < r_value:
        return 0
    return factorial_list[n_value] * inverse_list[n_value - r_value] % modulus * inverse_list[r_value] % modulus

input_n, input_x = map(int, input().split())
modulus_value = 998244353
factorial_list, inverse_list = calc_factorials_and_inverses(input_n + 15, modulus_value)
total_count = 0

for count_two in range(input_n + 1):
    for count_one in range(input_n + 1):
        if count_one + count_two > input_n:
            break
        total_distance = count_one + count_two * 2
        count_zero = calc_combination(input_n, count_one + count_two, modulus_value, factorial_list, inverse_list)
        current_count = 0

        if total_distance < input_x:
            current_count = calc_combination(count_one + count_two, count_one, modulus_value, factorial_list, inverse_list) * count_zero
        elif total_distance == input_x:
            continue
        elif total_distance < 2 * input_x:
            if (total_distance - input_x) % 2 == 0:
                continue
            adjusted_two = count_two - (total_distance - input_x + 1)
            if adjusted_two >= 0:
                current_count = calc_combination(count_one + adjusted_two, count_one, modulus_value, factorial_list, inverse_list) * count_zero
        elif input_x % 2 == 1 and count_one == 0:
            current_count = count_zero

        total_count = (total_count + current_count) % modulus_value

print(total_count)