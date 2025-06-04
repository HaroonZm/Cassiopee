import sys
sys.setrecursionlimit(10**9)
def_input = sys.stdin.readline

var_num_elements, var_target_parity = map(int, def_input().split())
arr_factorial = [1] * (var_num_elements + 1)
for idx_factorial in range(1, var_num_elements):
    arr_factorial[idx_factorial + 1] = arr_factorial[idx_factorial] * (idx_factorial + 1)

lst_parity_seq = list(map(lambda val: int(val) % 2, def_input().split()))

cnt_odd_elements = lst_parity_seq.count(1)
cnt_even_elements = var_num_elements - cnt_odd_elements

val_even_combinations = 2 ** cnt_even_elements
val_odd_select_even = sum([arr_factorial[cnt_odd_elements] // (arr_factorial[idx_select] * arr_factorial[cnt_odd_elements - idx_select]) for idx_select in range(0, cnt_odd_elements + 1, 2)])
val_odd_select_odd = sum([arr_factorial[cnt_odd_elements] // (arr_factorial[idx_select] * arr_factorial[cnt_odd_elements - idx_select]) for idx_select in range(1, cnt_odd_elements + 1, 2)])

val_final_answer = 0

if var_target_parity == 0:
    if val_even_combinations * val_odd_select_even != 0:
        val_final_answer = val_even_combinations * val_odd_select_even
    else:
        val_final_answer = max(val_even_combinations, val_odd_select_even)
else:
    if val_odd_select_odd == 0:
        val_final_answer = 0
    else:
        if val_even_combinations * val_odd_select_odd != 0:
            val_final_answer = val_even_combinations * val_odd_select_odd
        else:
            val_final_answer = max(val_even_combinations, val_odd_select_odd)

print(val_final_answer)