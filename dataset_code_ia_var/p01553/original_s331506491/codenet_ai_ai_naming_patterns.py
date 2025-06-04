MODULUS = 10**9 + 7
input_count = int(input())
state_dp = [[0 for state_j in range(input_count + 1)] for state_i in range(input_count + 1)]
state_dp[0][0] = 1

for index_i in range(1, input_count + 1):
    command_str = input()
    for index_j in range(input_count + 1):
        if command_str == "U":
            if index_j > 0:
                state_dp[index_i][index_j] += state_dp[index_i - 1][index_j - 1]
            state_dp[index_i][index_j] += index_j * state_dp[index_i - 1][index_j]
        elif command_str == "-":
            state_dp[index_i][index_j] += state_dp[index_i - 1][index_j]
        else:
            if index_j < input_count:
                state_dp[index_i][index_j] += (index_j + 1) * (index_j + 1) * state_dp[index_i - 1][index_j + 1]
            state_dp[index_i][index_j] += index_j * state_dp[index_i - 1][index_j]
        state_dp[index_i][index_j] %= MODULUS

print(state_dp[input_count][0])