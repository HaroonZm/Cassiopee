quantities_of_coins = list(map(int, input().split()))

quantity_1_yen_coins = quantities_of_coins[0]
quantity_5_yen_coins = quantities_of_coins[1]
quantity_10_yen_coins = quantities_of_coins[2]
quantity_50_yen_coins = quantities_of_coins[3]
quantity_100_yen_coins = quantities_of_coins[4]
quantity_500_yen_coins = quantities_of_coins[5]

total_amount_in_yen = (quantity_1_yen_coins * 1
                       + quantity_5_yen_coins * 5
                       + quantity_10_yen_coins * 10
                       + quantity_50_yen_coins * 50
                       + quantity_100_yen_coins * 100
                       + quantity_500_yen_coins * 500)

if total_amount_in_yen >= 1000:
    
    print(1)
    
else:
    
    print(0)