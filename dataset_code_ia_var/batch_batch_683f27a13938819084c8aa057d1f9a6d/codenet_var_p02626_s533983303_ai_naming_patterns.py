from functools import reduce, lru_cache

CONST_INF = float("inf")

input_values = list(map(int, open(0).read().split()))
var_count_n, var_start_a, var_start_b, *var_list_values = input_values
var_xor_c = reduce(lambda accumulator, element: accumulator ^ element, var_list_values, 0)

@lru_cache(None)
def calc_solution(param_a, param_b, param_c):
    if (param_a % 2) ^ (param_b % 2) != (param_c % 2):
        return CONST_INF
    if param_c == 0:
        return CONST_INF if param_a < param_b else (param_a - param_b) // 2
    res_direct = 2 * calc_solution(param_a // 2, param_b // 2, param_c // 2)
    res_adjust = 1 + 2 * calc_solution((param_a - 1) // 2, (param_b + 1) // 2, param_c // 2)
    return min(res_direct, res_adjust)

result_final = calc_solution(var_start_a, var_start_b, var_xor_c)
print(-1 if result_final >= var_start_a else result_final)