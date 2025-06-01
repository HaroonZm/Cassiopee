coins_values = (1, 5, 10, 50, 100, 500)

input_counts = input().split()

counts_as_integers = map(int, input_counts)

product_list = (coin * count for coin, count in zip(coins_values, counts_as_integers))

total_amount = sum(product_list)

if total_amount >= 1000:
    
    print(1)
    
else:
    
    print(0)