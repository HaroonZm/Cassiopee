import os
import sys
import numpy as np

def solve(input_array):
    def mod_power(base, exponent, modulus):
        result = 1
        factor = base
        while exponent:
            if exponent & 1:
                result = (result * factor) % modulus
            factor = (factor * factor) % modulus
            exponent >>= 1
        return result

    tree_height = input_array[0]
    leaf_nodes = input_array[1:]
    num_leaves = 1 << (tree_height - 1)
    leaf_nodes = np.append(leaf_nodes, np.arange(num_leaves - 1))
    modulus = 10 ** 9 + 7

    factorial_table = np.ones(2 * num_leaves, dtype=np.int64)
    inverse_factorial_table = np.ones(num_leaves, dtype=np.int64)
    path_product_table = np.zeros(num_leaves, dtype=np.int64)
    for node_index in range(2, 2 * num_leaves):
        factorial_table[node_index] = factorial_table[node_index >> 1] * node_index % modulus
    for leaf_index in range(num_leaves):
        inverse_factorial_table[leaf_index] = mod_power(factorial_table[leaf_index], modulus - 2, modulus)
        path_product_table[leaf_index] = factorial_table[leaf_index + num_leaves] * factorial_table[leaf_nodes[leaf_index]] % modulus

    temp_accumulator = np.zeros(2 * num_leaves, dtype=np.int64)
    result_value = 0

    for ancestor_node in range(1, num_leaves):
        depth_counter = ancestor_node
        bits_to_shift = tree_height
        while depth_counter:
            depth_counter >>= 1
            bits_to_shift -= 1

        leftmost_leaf_left = ancestor_node << bits_to_shift
        leftmost_leaf_right = ((ancestor_node << 1) + 1) << (bits_to_shift - 1)
        rightmost_leaf_right = (ancestor_node + 1) << bits_to_shift

        left_rev_factor = inverse_factorial_table[ancestor_node >> 1]
        for first_leaf in range(leftmost_leaf_left, leftmost_leaf_right):
            leaf_value = leaf_nodes[first_leaf - num_leaves]
            contribution = path_product_table[first_leaf - num_leaves] * left_rev_factor % modulus
            v = leaf_value
            while v > 1:
                temp_accumulator[v] = (temp_accumulator[v] + contribution * inverse_factorial_table[v >> 1] % modulus) % modulus
                v >>= 1

        right_rev_factor = inverse_factorial_table[ancestor_node]
        for second_leaf in range(leftmost_leaf_right, rightmost_leaf_right):
            leaf_value = leaf_nodes[second_leaf - num_leaves]
            contribution = path_product_table[second_leaf - num_leaves] * right_rev_factor % modulus
            v = leaf_value
            while v > 1:
                partial_res = temp_accumulator[v ^ 1] % modulus * contribution % modulus * inverse_factorial_table[v >> 2] % modulus
                result_value = (result_value + partial_res) % modulus
                v >>= 1

        for first_leaf in range(leftmost_leaf_left, leftmost_leaf_right):
            leaf_value = leaf_nodes[first_leaf - num_leaves]
            v = leaf_value
            while temp_accumulator[v] != 0:
                temp_accumulator[v] = 0
                v >>= 1

    return result_value

if sys.argv[-1] == 'ONLINE_JUDGE':
    from numba.pycc import CC
    compiler_instance = CC('main_module')
    compiler_instance.export('solve', '(i8[:],)')(solve)
    compiler_instance.compile()
    exit()

if os.name == 'posix':
    from main_module import solve
else:
    from numba import njit
    solve = njit('(i8[:],)', cache=True)(solve)
    print('compiled', file=sys.stderr)

input_array = np.fromstring(sys.stdin.read(), dtype=np.int64, sep=' ')
output_result = solve(input_array)
print(output_result)