coin_values = [1, 5, 10, 50, 100, 500]

while True:
    user_input = input().split()
    payment_amount = int(user_input[0])
    available_coins = list(map(int, user_input[1:]))

    minimum_total_coins_used = float('inf')

    if payment_amount == 0:
        break

    total_available_money = sum(
        coin_value * coin_count
        for coin_value, coin_count in zip(coin_values, available_coins)
    )

    for additional_change_to_give in range(1000):
        payment_required = payment_amount + additional_change_to_give
        coins_used_for_payment = [0] * len(coin_values)
        remaining_payment = payment_required

        # Try to pay using available coins, largest first
        for coin_index in reversed(range(len(coin_values))):
            if remaining_payment >= coin_values[coin_index]:
                coins_to_use = min(available_coins[coin_index], remaining_payment // coin_values[coin_index])
                coins_used_for_payment[coin_index] = coins_to_use
                remaining_payment -= coins_to_use * coin_values[coin_index]

        if remaining_payment > 0:
            break  # Not enough coins, stop checking further

        coins_given_for_payment = sum(coins_used_for_payment)

        # Now compute the minimum number of coins needed to give change (unlimited supply assumed)
        coins_needed_for_change = additional_change_to_give
        coins_used_for_change = 0

        for coin_index in reversed(range(len(coin_values))):
            if coins_needed_for_change >= coin_values[coin_index]:
                coins_used = coins_needed_for_change // coin_values[coin_index]
                coins_used_for_change += coins_used
                coins_needed_for_change %= coin_values[coin_index]

        total_coins_this_transaction = coins_given_for_payment + coins_used_for_change

        if total_coins_this_transaction < minimum_total_coins_used:
            minimum_total_coins_used = total_coins_this_transaction

    print(minimum_total_coins_used)