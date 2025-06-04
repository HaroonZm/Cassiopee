input_total_sum, input_max_part = map(int, input().split())
constant_modulus = 10**9 + 7
table_dp = [[0] * (input_total_sum + 1) for _ in range(input_max_part + 1)]
table_dp[0][0] = 1
for current_part in range(1, input_max_part + 1):
    for current_sum in range(input_total_sum + 1):
        if current_sum - current_part >= 0:
            table_dp[current_part][current_sum] = (table_dp[current_part - 1][current_sum] + table_dp[current_part][current_sum - current_part]) % constant_modulus
        else:
            table_dp[current_part][current_sum] = table_dp[current_part - 1][current_sum]
print(table_dp[input_max_part][input_total_sum])