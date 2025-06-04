input_n, input_k = map(int, input().split())
result_total = 0.0
for loop_i in range(1, input_n + 1):
    multiplier_t = 1
    while loop_i * multiplier_t < input_k:
        multiplier_t *= 2
    result_total += 1.0 / multiplier_t
average_result = result_total / input_n
print(average_result)