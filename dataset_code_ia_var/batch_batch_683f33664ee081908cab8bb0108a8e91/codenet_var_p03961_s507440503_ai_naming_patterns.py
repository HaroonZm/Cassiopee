MODULUS = 10 ** 9 + 7

def mod_inverse(value, modulus):
    return pow(value, modulus - 2, modulus)

def mod_factorial_tables(limit, modulus):
    factorial_table = [1] * (limit + 1)
    inverse_table = [1] * (limit + 1)
    fact = 1
    for idx in range(1, limit + 1):
        fact = (fact * idx) % modulus
        factorial_table[idx] = fact
    inv_fact = pow(fact, modulus - 2, modulus)
    inverse_table[limit] = inv_fact
    for idx in range(limit, 1, -1):
        inv_fact = (inv_fact * idx) % modulus
        inverse_table[idx - 1] = inv_fact
    return factorial_table, inverse_table

def mod_combination(n, r, modulus, factorial_table, inverse_table):
    return factorial_table[n] * inverse_table[n - r] * inverse_table[r] % modulus

def bit_add(position, increment, binary_indexed_tree):
    idx = position
    tree_size = len(binary_indexed_tree) - 1
    while idx <= tree_size:
        binary_indexed_tree[idx] += increment
        idx += idx & -idx

def bit_prefix_sum(position, binary_indexed_tree):
    result = 0
    idx = position
    while idx > 0:
        result += binary_indexed_tree[idx]
        idx -= idx & -idx
    return result

import sys
from sys import stdin

element_count = int(stdin.readline())
element_list = list(map(int, stdin.readline().split()))

binary_indexed_tree = [0] * (element_count + 1)

factorial_values, inverse_factorial_values = mod_factorial_tables(element_count + 10, MODULUS)
empty_count = 0
 
contribution_fixed = 0
right_empty_count = [0] * element_count
is_in_use = [False] * (element_count + 1)
is_in_use[0] = True

for element_idx in range(element_count - 1, -1, -1):
    if element_list[element_idx] != 0:
        contribution_fixed += factorial_values[element_count - 1 - element_idx] * bit_prefix_sum(element_list[element_idx], binary_indexed_tree)
        contribution_fixed %= MODULUS
        bit_add(element_list[element_idx], 1, binary_indexed_tree)
        is_in_use[element_list[element_idx]] = True
    else:
        empty_count += 1
    right_empty_count[element_idx] = empty_count

smaller_unused_count = [0] * (element_count + 1)
for num in range(1, element_count + 1):
    if not is_in_use[num]:
        smaller_unused_count[num] = smaller_unused_count[num - 1] + 1
    else:
        smaller_unused_count[num] = smaller_unused_count[num - 1]

contribution_fixed = (contribution_fixed * factorial_values[empty_count]) % MODULUS

contribution_mixed = 0
contribution_free = 0
empty_inverse = mod_inverse(empty_count, MODULUS)
free_factorial_sum = 0

for idx in range(element_count):
    if element_list[idx] != 0:
        contribution_mixed += factorial_values[empty_count] * smaller_unused_count[element_list[idx]] * right_empty_count[idx] * empty_inverse * factorial_values[element_count - 1 - idx]
        contribution_mixed += factorial_values[empty_count] * (empty_count - smaller_unused_count[element_list[idx]]) * empty_inverse * free_factorial_sum
        contribution_mixed %= MODULUS
    else:
        contribution_free += factorial_values[element_count - 1 - idx] * factorial_values[empty_count] * (right_empty_count[idx] - 1) * mod_inverse(2, MODULUS)
        free_factorial_sum += factorial_values[element_count - 1 - idx]

contribution_free %= MODULUS

print(contribution_fixed, contribution_mixed, contribution_free, factorial_values[empty_count], file=sys.stderr)
print((contribution_fixed + contribution_mixed + contribution_free + factorial_values[empty_count]) % MODULUS)