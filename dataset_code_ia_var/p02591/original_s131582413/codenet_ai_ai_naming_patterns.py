import sys

MOD_CONST = 10**9 + 7

HEIGHT = int(input())
TOURNAMENT_SIZE = 2 ** (HEIGHT - 1)
PLAYER_ORDER = list(map(lambda element: int(element) - 1, input().split()))
INVERSE_TWO = pow(2, MOD_CONST - 2, MOD_CONST)

SEQ_CNT = 1 + (1 << HEIGHT)

tree_mult = [1] * SEQ_CNT
tree_mult[0] = 0
for idx in range(2, SEQ_CNT):
    tree_mult[idx] = idx * tree_mult[idx >> 1] % MOD_CONST

tree_scal = [ (idx * pow(tree_mult[idx] ** 2, MOD_CONST - 2, MOD_CONST)) % MOD_CONST for idx in range(SEQ_CNT) ]

res_final = 0

def recursive_solve(node_idx):
    global res_final
    if node_idx >= TOURNAMENT_SIZE:
        idx_inner = node_idx - TOURNAMENT_SIZE
        prod_ab = (tree_mult[idx_inner + TOURNAMENT_SIZE] * tree_mult[PLAYER_ORDER[idx_inner] + TOURNAMENT_SIZE]) % MOD_CONST
        prod_square = pow(prod_ab, 2, MOD_CONST)
        ident = PLAYER_ORDER[idx_inner] + TOURNAMENT_SIZE
        base_data = [ [ident >> (HEIGHT - 1 - j), prod_ab, prod_square] for j in range(HEIGHT) ]
        return base_data
    left_vals = recursive_solve(2 * node_idx)
    right_vals = recursive_solve(2 * node_idx + 1)
    merged_vals, partial = merge_lists(left_vals, right_vals)
    partial = partial * (tree_scal[node_idx] - tree_scal[node_idx >> 1]) % MOD_CONST
    res_final = (res_final + partial) % MOD_CONST
    return merged_vals

def merge_lists(list_left, list_right):
    merged_list = []
    list_left.append([float('inf'), 0])
    list_right.append([float('inf'), 0])
    list_left = list_left[::-1]
    list_right = list_right[::-1]
    sum_partial = 0
    if list_left[-1][0] <= list_right[-1][0]:
        merged_list.append(list_left.pop())
    else:
        merged_list.append(list_right.pop())
    while list_left and list_right:
        if list_left[-1][0] <= list_right[-1][0]:
            if merged_list and merged_list[-1][0] == list_left[-1][0]:
                merged_list[-1][1] = (merged_list[-1][1] + list_left[-1][1]) % MOD_CONST
                merged_list[-1][2] = (merged_list[-1][2] + list_left[-1][2]) % MOD_CONST
                list_left.pop()
            else:
                ident, accum, accum_sq = merged_list[-1]
                scal_term = (tree_scal[ident] - tree_scal[ident >> 1]) % MOD_CONST
                temp_val = (accum ** 2 % MOD_CONST - accum_sq) % MOD_CONST
                all_term = (scal_term * temp_val) % MOD_CONST
                sum_partial = (sum_partial + all_term) % MOD_CONST
                merged_list.append(list_left.pop())
        else:
            if merged_list and merged_list[-1][0] == list_right[-1][0]:
                merged_list[-1][1] = (merged_list[-1][1] + list_right[-1][1]) % MOD_CONST
                merged_list[-1][2] = (merged_list[-1][2] + list_right[-1][2]) % MOD_CONST
                list_right.pop()
            else:
                ident, accum, accum_sq = merged_list[-1]
                scal_term = (tree_scal[ident] - tree_scal[ident >> 1]) % MOD_CONST
                temp_val = (accum ** 2 % MOD_CONST - accum_sq) % MOD_CONST
                all_term = (scal_term * temp_val) % MOD_CONST
                sum_partial = (sum_partial + all_term) % MOD_CONST
                merged_list.append(list_right.pop())
    merged_list.pop()
    return merged_list, sum_partial

recursive_solve(1)
print(res_final * INVERSE_TWO % MOD_CONST)