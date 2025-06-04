from collections import Counter
from itertools import accumulate

input_num_a, input_num_b = map(int, input().split())
list_a = list(map(int, input().split()))
list_b = list(map(int, input().split()))

max_value = max(list_a)
value_table = [0] * (max_value + 1)

value_table[0] = input_num_b

counter_b = Counter(list_b)
for b_key, b_count in counter_b.items():
    for idx_minus in range(b_key, max_value + 1, b_key):
        value_table[idx_minus] -= b_key * b_count
    for idx_plus in range(b_key + 1, max_value + 1, b_key):
        value_table[idx_plus] += b_key * b_count

value_table = list(accumulate(value_table))
value_table[0] = 0
value_table = list(accumulate(value_table))

result_sum = sum(value_table[a_value] for a_value in list_a)
print(result_sum)