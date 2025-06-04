N = int(input())
nums = list(map(int, input().split()))

dp = [[[0]*(21) for _ in range(21)] for _ in range(N-1)]
# dp[i][s][v] = nombre de façons d'obtenir la valeur v après avoir utilisé les nombres jusqu'à i (de 0 à i) avec un résultat partiel s

dp[0][nums[0]][nums[0]] = 1

for i in range(1, N-1):
    for prev_val in range(21):
        for curr_sum in range(21):
            if dp[i-1][prev_val][curr_sum] > 0:
                # essayer +
                new_sum = curr_sum + nums[i]
                if 0 <= new_sum <= 20:
                    dp[i][nums[i]][new_sum] += dp[i-1][prev_val][curr_sum]
                # essayer -
                new_sum = curr_sum - nums[i]
                if 0 <= new_sum <= 20:
                    dp[i][nums[i]][new_sum] += dp[i-1][prev_val][curr_sum]

result = 0
last = nums[-1]

for prev_val in range(21):
    for curr_sum in range(21):
        if dp[N-2][prev_val][curr_sum] > 0:
            if curr_sum == last:
                result += dp[N-2][prev_val][curr_sum]

print(result)