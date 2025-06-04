input_values_count, input_values_k = map(int, input().split())
modulus_constant = 10**9 + 7
result_answer = 1 if input_values_k >= input_values_count else 0
print(result_answer)