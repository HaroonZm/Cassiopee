import sys

def read_input_line_and_strip_whitespace():
    return sys.stdin.readline().strip()

def create_2d_list(num_rows, num_columns, initial_value):
    return [[initial_value] * num_columns for _ in range(num_rows)]

def create_3d_list(num_rows, num_columns, depth, initial_value):
    return [[[initial_value] * depth for _ in range(num_columns)] for _ in range(num_rows)]

def create_4d_list(dim1, dim2, dim3, dim4, initial_value):
    return [[[[initial_value] * dim4 for _ in range(dim3)] for _ in range(dim2)] for _ in range(dim1)]

def compute_ceiling_division(numerator, denominator=1):
    return int(-(-numerator // denominator))

def read_single_integer():
    return int(read_input_line_and_strip_whitespace())

def read_space_separated_integers():
    return map(int, read_input_line_and_strip_whitespace().split())

def read_integer_list(number_of_elements=None):
    if number_of_elements is None:
        return list(read_space_separated_integers())
    else:
        return [read_single_integer() for _ in range(number_of_elements)]

def print_yes_with_capital_y():
    print('Yes')

def print_no_with_capital_n():
    print('No')

def print_yes_all_caps():
    print('YES')

def print_no_all_caps():
    print('NO')

sys.setrecursionlimit(10**9)
INFINITY_REPRESENTATION = 10 ** 18
MODULUS_FOR_PROBLEMS = 10 ** 9 + 7
EPSILON_FOR_FLOAT_COMPARISON = 10 ** -10

class ModuloArithmeticTools:
    """Pré-calcul pour les combinaisons, permutations et inverses modulo MODULUS_FOR_PROBLEMS"""

    def __init__(self, maximum_value_for_tables, modulus):
        
        maximum_value_for_tables += 1
        self.maximum_value_for_tables = maximum_value_for_tables
        self.modulus = modulus

        factorial_table = [1] * maximum_value_for_tables
        factorial_table[0] = factorial_table[1] = 1

        for current_value in range(2, maximum_value_for_tables):
            factorial_table[current_value] = (
                factorial_table[current_value - 1] 
                * current_value 
                % modulus
            )

        inverse_table = [1] * maximum_value_for_tables
        inverse_table[-1] = pow(factorial_table[-1], modulus - 2, modulus)

        for current_value in range(maximum_value_for_tables - 2, -1, -1):
            inverse_table[current_value] = (
                inverse_table[current_value + 1]
                * (current_value + 1)
                % modulus
            )

        self.factorial_table = factorial_table
        self.inverse_table = inverse_table

    def compute_binomial_coefficient_nCr(self, n, r):
        """Calcul du coefficient binomial (combinaisons)"""

        if n < r:
            return 0

        r = min(r, n - r)

        numerator = self.factorial_table[n]
        denominator = (
            self.inverse_table[r] 
            * self.inverse_table[n - r] 
            % self.modulus
        )

        return numerator * denominator % self.modulus

    def compute_multichoose_nHr(self, n, r):
        """Calcul du nombre de multichoix"""

        return self.compute_binomial_coefficient_nCr(r + n - 1, r)

    def compute_permutation_nPr(self, n, r):
        """Calcul du nombre de permutations (nPr)"""

        if n < r:
            return 0

        return (
            self.factorial_table[n]
            * self.inverse_table[n - r]
            % self.modulus
        )

    def perform_modular_division(self, dividend, divisor):
        """Division modulaire"""

        return dividend * pow(divisor, self.modulus - 2, self.modulus) % self.modulus

number_of_items, number_of_selections = read_space_separated_integers()

modulo_arithmetic_tools = ModuloArithmeticTools(
    number_of_items + number_of_selections + 1,
    MODULUS_FOR_PROBLEMS
)

resulting_binomial_coefficient = modulo_arithmetic_tools.compute_binomial_coefficient_nCr(
    number_of_selections,
    number_of_items
)

print(resulting_binomial_coefficient)