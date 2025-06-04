from string import digits as DIGIT_CHARACTERS, ascii_uppercase as UPPERCASE_LETTERS

def parse_permutation_expression(
    permutation_expression: str,
    permutation_size: int,
    permutation_definitions: dict
):
    current_index_in_expression = 0
    permutation_expression = permutation_expression + "$"

    def parse_sum_expression():
        nonlocal current_index_in_expression

        result_permutation = list(range(permutation_size))

        while True:
            term_permutation = parse_term()
            result_permutation[:] = [
                result_permutation[element]
                for element in term_permutation
            ]
            if permutation_expression[current_index_in_expression] != '+':
                break
            current_index_in_expression += 1  # skip '+'
        return result_permutation

    def parse_term():
        nonlocal current_index_in_expression

        if permutation_expression[current_index_in_expression] in DIGIT_CHARACTERS:
            exponent = read_integer()
            if permutation_expression[current_index_in_expression] == '(':
                current_index_in_expression += 1  # skip '('
                inner_permutation = parse_sum_expression()
                current_index_in_expression += 1  # skip ')'
            else:
                inner_permutation = get_identity_permutation()
            result_permutation = apply_permutation_power(inner_permutation, exponent)
        else:
            result_permutation = get_identity_permutation()
        return result_permutation

    def apply_permutation_power(permutation, power):
        current_result = list(range(permutation_size))
        power_permutation = permutation[:]
        while power:
            if power & 1:
                current_result[:] = [current_result[index] for index in power_permutation]
            power_permutation[:] = [power_permutation[index] for index in power_permutation]
            power >>= 1
        return current_result

    def read_integer():
        nonlocal current_index_in_expression

        integer_value = 0
        while permutation_expression[current_index_in_expression] in DIGIT_CHARACTERS:
            integer_value = integer_value * 10 + int(permutation_expression[current_index_in_expression])
            current_index_in_expression += 1
        return integer_value

    def get_identity_permutation():
        nonlocal current_index_in_expression
        permutation_name = permutation_expression[current_index_in_expression]
        permutation_vector = permutation_definitions[permutation_name]
        current_index_in_expression += 1  # skip permutation name
        return permutation_vector

    return parse_sum_expression()

def main():
    permutation_size, number_of_permutations = map(int, input().split())
    permutation_definitions = {}

    for _ in range(number_of_permutations):
        permutation_name, number_of_layers = input().split()
        number_of_layers = int(number_of_layers)
        current_permutation = list(range(permutation_size))
        for _ in range(number_of_layers - 1):
            swaps = list(map(int, input().split()))
            for idx in range(permutation_size - 1):
                if swaps[idx]:
                    current_permutation[idx], current_permutation[idx + 1] = (
                        current_permutation[idx + 1], current_permutation[idx]
                    )
        permutation_definitions[permutation_name] = current_permutation

    number_of_expressions = int(input())
    for _ in range(number_of_expressions):
        input_expression = input()
        result_permutation = parse_permutation_expression(
            input_expression,
            permutation_size,
            permutation_definitions
        )
        print(*[element + 1 for element in result_permutation])

main()