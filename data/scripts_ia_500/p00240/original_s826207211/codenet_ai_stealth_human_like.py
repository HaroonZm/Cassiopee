while True:
    max_profit = 0
    best_id = 0
    n = int(input())  # number of entries
    if n == 0:
        break
    years = int(input())
    data = []
    for _ in range(n):
        data.append(list(map(int, input().split())))
    
    for entry in data:
        id_val = entry[0]
        rate = entry[1]
        typ = entry[2]
        
        if typ == 1:
            profit = 1 + (years * rate / 100)  # simple interest kinda
        else:
            profit = (1 + rate / 100) ** years  # compound interest
        
        if profit > max_profit:
            max_profit = profit
            best_id = id_val
    print(best_id)