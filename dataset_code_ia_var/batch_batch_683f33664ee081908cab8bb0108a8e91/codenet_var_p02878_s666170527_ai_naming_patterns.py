input_n, input_a, input_b = map(int, input().split())
modulo = 998244353
seq_len = input_n + 1
factorial_acc = 1
factorial_list = [1] * seq_len
inverse_list = [1] * seq_len
result_sum = 0
range_seq = range

for cur_index in range_seq(1, seq_len):
    factorial_list[cur_index] = factorial_acc = factorial_acc * cur_index % modulo

inverse_list[input_n] = inverse_acc = pow(factorial_acc, modulo - 2, modulo)
for cur_index in range_seq(input_n, 1, -1):
    inverse_list[cur_index - 1] = inverse_acc = inverse_acc * cur_index % modulo

if input_n - input_b - input_a:
    loop_range = min(input_a + 1, input_n - input_b)
else:
    loop_range = input_a + 1

for cur_k in range_seq(loop_range):
    param_q = input_n - input_b - cur_k - 1
    add_term = (input_b - cur_k) \
        * factorial_list[input_b + cur_k - 1] \
        * inverse_list[input_b] \
        * inverse_list[cur_k] \
        * factorial_list[param_q + input_a - cur_k] \
        * inverse_list[param_q] \
        * inverse_list[input_a - cur_k]
    result_sum = (result_sum + add_term) % modulo

print(result_sum if input_b else 1)