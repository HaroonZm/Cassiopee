import sys
sys.setrecursionlimit(10**7)

def compute_value(param_a, param_b):
    if param_a == param_b:
        return param_a
    if param_a > param_b:
        param_a, param_b = param_b, param_a
    if param_b % param_a == 0:
        return 2 * (param_b // param_a) * param_a - param_a
    return 2 * (param_b // param_a) * param_a + compute_value(param_a, param_b % param_a)

input_total, input_position = map(int, input().split())
result = compute_value(input_position, input_total - input_position) + input_total
print(result)