# AOJ 0240: Interest Rates
# Python3 solution from 2018 by bal4u

while True:
    n = int(input())
    if n == 0:
        break
    y = float(input())
    
    best_bank = -1
    best_value = 0
    for _ in range(n):
        bank_id, rate, t = map(int, input().split())
        
        # Calculate multiplier depending on type of interest
        if t == 1:
            mult = y * (rate / 100) + 1  # simple interest
        else:
            mult = (1 + rate / 100) ** y  # compound interest
        
        # Update if this bank's multiplier is better or if first iteration
        if best_bank < 0 or mult >= best_value:
            best_bank, best_value = bank_id, mult
    
    print(best_bank)