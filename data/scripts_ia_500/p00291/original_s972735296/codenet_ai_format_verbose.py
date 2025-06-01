coin_values = [1, 5, 10, 50, 100, 500]

if __name__ == "__main__":

    coin_counts_in_wallet = list(map(int, input().split()))

    total_amount_in_wallet = 0

    for index in range(len(coin_values)):

        coin_value = coin_values[index]

        coin_count = coin_counts_in_wallet[index]

        total_amount_in_wallet += coin_value * coin_count

    if total_amount_in_wallet >= 1000:
        print(1)
    else:
        print(0)