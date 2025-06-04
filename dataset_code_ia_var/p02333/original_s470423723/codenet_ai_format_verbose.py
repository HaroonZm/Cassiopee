import sys

def read_input_line():
    return sys.stdin.readline().strip()

def create_2d_list(rows, columns, default_value):
    return [[default_value] * columns for _ in range(rows)]

def create_3d_list(dim1, dim2, dim3, default_value):
    return [[[default_value] * dim3 for _ in range(dim2)] for _ in range(dim1)]

def create_4d_list(dim1, dim2, dim3, dim4, default_value):
    return [[[[default_value] * dim4 for _ in range(dim3)] for _ in range(dim2)] for _ in range(dim1)]

def ceil_divide(numerator, denominator=1):
    return int(-(-numerator // denominator))

def read_single_integer():
    return int(read_input_line())

def read_integer_map():
    return map(int, read_input_line().split())

def read_integer_list(expected_count=None):
    if expected_count is None:
        return list(read_integer_map())
    else:
        return [read_single_integer() for _ in range(expected_count)]

def print_Yes():
    print('Yes')

def print_No():
    print('No')

def print_YES():
    print('YES')

def print_NO():
    print('NO')

sys.setrecursionlimit(10 ** 9)

INFINITY = 10 ** 18
MODULUS = 10 ** 9 + 7
EPSILON = 10 ** -10

class ModularCombinatoricsTable:
    """ Calculates factorial, modular inverses, and combinatorics efficiently (mod MODULUS) """

    def __init__(self, maximum_value, modulus):
        maximum_value += 1
        self.maximum_value = maximum_value
        self.modulus = modulus

        self.factorials = [1] * maximum_value
        self.factorials[0] = 1
        self.factorials[1] = 1
        for index in range(2, maximum_value):
            self.factorials[index] = self.factorials[index - 1] * index % modulus

        self.inverse_factorials = [1] * maximum_value
        self.inverse_factorials[maximum_value - 1] = pow(self.factorials[maximum_value - 1], modulus - 2, modulus)
        for index in range(maximum_value - 2, -1, -1):
            self.inverse_factorials[index] = self.inverse_factorials[index + 1] * (index + 1) % modulus

    def combination(self, n, r):
        """ Number of n choose r (nCr) (mod modulus) """
        if n < r:
            return 0
        r = min(r, n - r)
        numerator = self.factorials[n]
        denominator = self.inverse_factorials[r] * self.inverse_factorials[n - r] % self.modulus
        return numerator * denominator % self.modulus

    def multichoose(self, n, r):
        """ Number of multisets of size r from n types (nHr) (mod modulus) """
        return self.combination(r + n - 1, r)

    def permutation(self, n, r):
        """ Number of n permute r (nPr) (mod modulus) """
        if n < r:
            return 0
        return self.factorials[n] * self.inverse_factorials[n - r] % self.modulus

    def modular_divide(self, numerator, denominator):
        """ Division modulo modulus """
        return numerator * pow(denominator, self.modulus - 2, self.modulus) % self.modulus

number_of_elements, number_of_colors = read_integer_map()

combinatorics_table = ModularCombinatoricsTable(max(number_of_elements, number_of_colors) + 1, MODULUS)

inclusion_exclusion_result = 0

for subset_size in range(number_of_colors + 1):

    count_subsets = combinatorics_table.combination(number_of_colors, subset_size)
    ways_to_color = pow(number_of_colors - subset_size, number_of_elements, MODULUS)
    current_term = count_subsets * ways_to_color % MODULUS

    if subset_size % 2 == 0:
        inclusion_exclusion_result += current_term
    else:
        inclusion_exclusion_result -= current_term

print(inclusion_exclusion_result % MODULUS)