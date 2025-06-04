coin_values = [10, 50, 100, 500]

def min_coins_change(amount):
    # Compute minimal coins for change (unlimited coins of each type)
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    for v in coin_values:
        for i in range(v, amount + 1, 10):
            if dp[i - v] + 1 < dp[i]:
                dp[i] = dp[i - v] + 1
    return dp

def get_change_coins(amount, dp):
    # Retrieve coins count for change using dp table
    res = [0,0,0,0]
    for i in range(3, -1, -1):
        v = coin_values[i]
        while amount >= v and dp[amount] == dp[amount - v] + 1:
            res[i] += 1
            amount -= v
    return res

def main():
    first_case = True
    while True:
        cost_line = input().strip()
        if cost_line == "0":
            break
        cost = int(cost_line)
        wallet = list(map(int, input().strip().split()))
        total_coins = sum(wallet)
        min_total = float('inf')
        best_pay = None  # Stores how many coins for each denomination to pay
        
        max_pay_10 = min(wallet[0], cost // 10)
        max_pay_50 = min(wallet[1], cost // 50)
        max_pay_100 = min(wallet[2], cost // 100)
        max_pay_500 = min(wallet[3], cost // 500)
        
        # Precompute minimal coins for change for all possible change amounts
        max_change = sum([wallet[i]*coin_values[i] for i in range(4)]) - cost
        change_dp = min_coins_change(max_change)
        
        # Enumerate ways to pay (bounded knapsack with 4 coins types, max 20 coins each)
        # We use 4 nested loops as max 20 per coin, manageable
        for c500 in range(max_pay_500 + 1):
            v500 = c500 * 500
            if v500 > cost:
                break
            remain1 = cost - v500
            for c100 in range(min(max_pay_100, remain1 // 100) + 1):
                v100 = c100 * 100
                if v500 + v100 > cost:
                    break
                remain2 = cost - v500 - v100
                for c50 in range(min(max_pay_50, remain2 // 50) + 1):
                    v50 = c50 * 50
                    if v500 + v100 + v50 > cost:
                        break
                    remain3 = cost - v500 - v100 - v50
                    # c10 determined by remain3 // 10
                    c10 = remain3 // 10
                    if c10 > max_pay_10:
                        continue
                    pay_value = v500 + v100 + v50 + c10 * 10
                    if pay_value != cost:
                        continue
                    
                    pay_coins = [c10, c50, c100, c500]
                    
                    # Condition: no coin kind used in pay is also given as change
                    # Compute change = total money he has - cost
                    # Total money in wallet:
                    total_money = 0
                    for i in range(4):
                        total_money += wallet[i] * coin_values[i]
                    change_value = total_money - cost
                    if change_value < 0:
                        continue
                    
                    # Compute wallet coins left after paying
                    left_coins = [wallet[i] - pay_coins[i] for i in range(4)]
                    # Calculate minimal coins for change_value with infinite coins (dp computed)
                    if change_value > max_change:
                        continue
                    if change_dp[change_value] == float('inf'):
                        continue
                    change_coins = get_change_coins(change_value, change_dp)
                    
                    # Confirm no coin used in pay is returned in change
                    conflict = False
                    for i in range(4):
                        if pay_coins[i] > 0 and change_coins[i] > 0:
                            conflict = True
                            break
                    if conflict:
                        continue
                    # total coins after operation = coins left + coins returned as change
                    total_after = sum(left_coins) + sum(change_coins)
                    if total_after < min_total:
                        min_total = total_after
                        best_pay = pay_coins[:]
        
        # Output according to required format
        # only output lines for coin used > 0 with small to large coin value order
        if not first_case:
            print()
        first_case = False
        for i in range(4):
            if best_pay[i] > 0:
                print(coin_values[i], best_pay[i])

if __name__ == "__main__":
    main()