from collections import defaultdict
import sys

def input_line():
    return sys.stdin.readline().rstrip()

def extended_euclidean_algorithm(a_value, b_value):
    x_prev, y_prev, remainder_prev = 1, 0, a_value
    x_curr, y_curr, remainder_curr = 0, 1, b_value
    while remainder_prev != 1:
        quotient, remainder_new = divmod(remainder_curr, remainder_prev)
        x_prev, x_curr = x_curr - quotient * x_prev, x_prev
        y_prev, y_curr = y_curr - quotient * y_prev, y_prev
        remainder_prev, remainder_curr = remainder_new, remainder_prev
    return x_prev, y_prev

class ModularInteger(int):
    def __new__(cls, value=0, *args, **kwargs):
        return int.__new__(cls, value % MODULUS, *args, **kwargs)

    def __add__(self, other):
        return self.__class__(int.__add__(self, other))

    def __sub__(self, other):
        return self.__class__(int.__sub__(self, other))

    def __neg__(self):
        return self.__class__(int.__neg__(self))

    def __mul__(self, other):
        return self.__class__(int.__mul__(self, other))

    def __floordiv__(self, other):
        inv, _ = extended_euclidean_algorithm(other, MODULUS)
        return self * inv

    def __pow__(self, exponent):
        return self.__class__(int.__pow__(self, exponent, MODULUS))

def minimum_excludant(values_set):
    for candidate in range(GLOBAL_N + 1):
        if candidate not in values_set:
            return candidate

def grundy_calculation(edge_dict):
    grundy_dict = {}
    for index in range(GLOBAL_N, 0, -1):
        if index not in edge_dict:
            continue
        mex_set = {grundy_dict.get(neigh, 0) for neigh in edge_dict[index]}
        grundy_value = minimum_excludant(mex_set)
        if grundy_value:
            grundy_dict[index] = grundy_value
    grundy_sum = defaultdict(ModularInteger)
    grundy_sum[0] = (GLOBAL_BASIS**(GLOBAL_N + 1) - GLOBAL_BASIS) // (GLOBAL_BASIS - 1)
    previous_index = 0
    cumulative_weight = ModularInteger(1)
    for index in range(1, GLOBAL_N + 1):
        if index in grundy_dict:
            cumulative_weight *= GLOBAL_BASIS ** (index - previous_index)
            grundy_sum[grundy_dict[index]] += cumulative_weight
            grundy_sum[0] -= cumulative_weight
            previous_index, cumulative_weight = index, cumulative_weight
    return grundy_sum

def edge_reader():
    edge_count = int(input_line())
    edge_structure = defaultdict(list)
    for edge_index in range(edge_count):
        node_a, node_b = sorted(map(int, input_line().split()))
        edge_structure[node_a].append(node_b)
    return edge_structure

def problem_solver(node_count, edges_list):
    grundy_sums = list(map(grundy_calculation, edges_list))
    result_sum = ModularInteger(0)
    for grundy_x, sum_x in grundy_sums[0].items():
        for grundy_y, sum_y in grundy_sums[1].items():
            grundy_z = grundy_x ^ grundy_y
            sum_z = grundy_sums[2][grundy_z]
            if sum_z:
                result_sum += sum_x * sum_y * sum_z
    return result_sum

MODULUS = 998244353
GLOBAL_BASIS = ModularInteger(10) ** 18
GLOBAL_N = int(input_line())

EDGE_LIST = [edge_reader() for _ in range(3)]

print(problem_solver(GLOBAL_N, EDGE_LIST))