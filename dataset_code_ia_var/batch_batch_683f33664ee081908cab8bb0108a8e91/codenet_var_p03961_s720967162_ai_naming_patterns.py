import sys

def read_input():
    return sys.stdin.readline().rstrip()

def set_recursion_limit_custom():
    sys.setrecursionlimit(max(1000, 10 ** 9))

def write_output(msg):
    sys.stdout.write(msg + "\n")

MOD_CONST = 10 ** 9 + 7
read_single_int = lambda: int(read_input())
read_int_list = lambda: list(map(int, read_input().split()))

set_recursion_limit_custom()
n_count = read_single_int()
perm_list = read_int_list()

fact_list = [None] * (n_count + 10)
fact_val = 1
fact_list[0] = 1
for fact_idx in range(1, len(fact_list)):
    fact_val = (fact_val * fact_idx) % MOD_CONST
    fact_list[fact_idx] = fact_val

def fenwick_add(bit_arr, idx, delta):
    if idx == 0:
        raise RuntimeError
    while idx <= len(bit_arr) - 1:
        bit_arr[idx] += delta
        idx += idx & -idx

def fenwick_query(bit_arr, idx):
    result = 0
    while idx > 0:
        result += bit_arr[idx]
        idx -= idx & -idx
    return result

def fenwick_initialize(bit_arr, vals):
    for idx, val in enumerate(vals):
        fenwick_add(bit_arr, idx + 1, val)

zero_indices = [i for i, num in enumerate(perm_list) if num == 0]
marked_used = [False] * n_count
for idx in range(n_count):
    if perm_list[idx] > 0:
        marked_used[perm_list[idx] - 1] = True

missing_list = []
for idx in range(n_count):
    if not marked_used[idx]:
        missing_list.append(idx + 1)
missing_list.sort()

greater_counter = [0] * (n_count + 1)
remain_val = len(missing_list)
cur_pos = 0
for i in range(1, n_count + 1):
    if missing_list and cur_pos < len(missing_list) and missing_list[cur_pos] < i:
        cur_pos += 1
        remain_val -= 1
    greater_counter[i] = remain_val

total_ans = 0
fenwick_tree = [0] * (n_count + 1)
zero_index_set = set(zero_indices)
partial_sum = 0
missing_count = len(zero_indices)
missing_sum = sum(missing_list)
missing_encountered = 0
inv_two = pow(2, MOD_CONST - 2, MOD_CONST)

for idx in range(n_count):
    if idx in zero_index_set:
        coeff = (fact_list[missing_count - 1] *
                 (missing_sum - missing_count - partial_sum - missing_count * (missing_encountered) * inv_two))
        total_ans += coeff * fact_list[n_count - idx - 1]
        missing_encountered += 1
    else:
        var_a = fact_list[missing_count] * (perm_list[idx] - fenwick_query(fenwick_tree, perm_list[idx]) - 1)
        var_b = fact_list[missing_count - 1] * missing_encountered * (len(missing_list) - greater_counter[perm_list[idx]])
        total_ans += (var_a - var_b) * fact_list[n_count - idx - 1]
        fenwick_add(fenwick_tree, perm_list[idx], 1)
        partial_sum += greater_counter[perm_list[idx]]
    total_ans %= MOD_CONST

write_output(str((total_ans + fact_list[missing_count]) % MOD_CONST))