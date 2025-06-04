import sys
io_input = sys.stdin.readline
io_output = sys.stdout.write

CONST_MOD = 10**9 + 7

CONST_LIMIT = 4 * 10**6
pre_fact = [1] * (CONST_LIMIT + 1)
pre_inv_fact = [1] * (CONST_LIMIT + 1)
curr_prod = 1
for idx in range(1, CONST_LIMIT + 1):
    pre_fact[idx] = curr_prod = curr_prod * idx % CONST_MOD
pre_inv_fact[CONST_LIMIT] = curr_prod = pow(pre_fact[CONST_LIMIT], CONST_MOD - 2, CONST_MOD)
for idx in range(CONST_LIMIT, 0, -1):
    pre_inv_fact[idx - 1] = curr_prod = curr_prod * idx % CONST_MOD

def task_process():
    var_a, var_b, var_c, start_x, start_y = map(int, io_input().split())
    if var_a + var_b + var_c == 0:
        return False
    if not start_x > start_y:
        var_a, var_b = var_b, var_a
        start_x, start_y = start_y, start_x
    delta_s = start_x - start_y
    max_iter = start_y
    is_zero = False
    if var_a == 0:
        if var_b > 0 or delta_s != 0:
            is_zero = True
        else:
            max_iter = 0
    elif var_b == 0:
        max_iter = 0

    if is_zero:
        io_output("0\n")
        return True

    ans_res = 0
    for loop_k in range(max_iter + 1):
        if delta_s + loop_k < var_a or loop_k < var_b:
            continue
        temp_val = pre_fact[delta_s + loop_k - 1] * pre_inv_fact[delta_s + loop_k - var_a] % CONST_MOD
        temp_val = temp_val * (pre_fact[loop_k - 1] * pre_inv_fact[loop_k - var_b] % CONST_MOD) % CONST_MOD
        temp_val = temp_val * (pre_fact[start_y - loop_k + var_a + var_b + var_c - 1] * pre_inv_fact[start_y - loop_k] % CONST_MOD) % CONST_MOD
        ans_res += temp_val
    ans_res %= CONST_MOD
    ans_res = ans_res * (pre_fact[var_a + var_b + var_c] * pre_inv_fact[var_a] % CONST_MOD) % CONST_MOD
    ans_res = ans_res * (pre_inv_fact[var_b] * pre_inv_fact[var_c] % CONST_MOD) % CONST_MOD
    ans_res = ans_res * (pre_inv_fact[var_a - 1] * pre_inv_fact[var_b - 1] % CONST_MOD) % CONST_MOD
    ans_res = ans_res * pre_inv_fact[var_a + var_b + var_c - 1] % CONST_MOD
    io_output("%d\n" % ans_res)
    return True

while task_process():
    pass