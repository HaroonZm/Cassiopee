MODULO = 10**9 + 7

total_steps, required_cost = map(int, input().split())

# dp[current_step][balance][current_cost] = number of ways
dp = [
    [
        [0] * (total_steps ** 2 + 1)
        for _ in range(total_steps + 1)
    ]
    for _ in range(total_steps + 1)
]

dp[0][0][0] = 1

for current_step in range(1, total_steps + 1):

    for current_balance in range(current_step + 1):

        for current_cost in range(total_steps ** 2 + 1):

            previous_cost = current_cost - 2 * current_balance

            if previous_cost < 0:
                continue

            # Continue with same balance
            ways_with_same_balance = (2 * current_balance + 1) * dp[current_step - 1][current_balance][previous_cost]
            dp[current_step][current_balance][current_cost] = ways_with_same_balance

            # Increase balance (open one more)
            if current_balance + 1 <= total_steps:
                ways_with_increased_balance = (current_balance + 1) ** 2 * dp[current_step - 1][current_balance + 1][previous_cost]
                dp[current_step][current_balance][current_cost] += ways_with_increased_balance

            # Decrease balance (close one)
            if current_balance - 1 >= 0:
                ways_with_decreased_balance = dp[current_step - 1][current_balance - 1][previous_cost]
                dp[current_step][current_balance][current_cost] += ways_with_decreased_balance

            dp[current_step][current_balance][current_cost] %= MODULO

print(dp[total_steps][0][required_cost])