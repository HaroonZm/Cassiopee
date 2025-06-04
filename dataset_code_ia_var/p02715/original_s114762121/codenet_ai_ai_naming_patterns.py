import sys

input_stream = sys.stdin

read_line_stripped = lambda: input_stream.readline().rstrip()
read_line_ints = lambda: list(map(int, input_stream.readline().split()))
read_line_int = lambda: int(read_line_stripped())

input_n, input_k = read_line_ints()
modulo_base = 1000000007

result_array = [0]
for current_divisor in range(1, input_k + 1):
    result_array.append(pow(input_k // current_divisor, input_n, modulo_base))

for index_divisor in range(input_k, 0, -1):
    multiple_divisor = 2 * index_divisor
    while multiple_divisor <= input_k:
        result_array[index_divisor] -= result_array[multiple_divisor]
        multiple_divisor += index_divisor
    if result_array[index_divisor] < 0:
        result_array[index_divisor] %= modulo_base
        if result_array[index_divisor] < 0:
            result_array[index_divisor] += modulo_base

final_answer = 0
for index_sum in range(1, input_k + 1):
    final_answer += index_sum * result_array[index_sum]
print(final_answer % modulo_base)