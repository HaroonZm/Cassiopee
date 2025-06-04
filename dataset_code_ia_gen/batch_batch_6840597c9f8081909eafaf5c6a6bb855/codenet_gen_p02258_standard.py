n = int(input())
rates = [int(input()) for _ in range(n)]
min_rate = rates[0]
max_profit = rates[1] - rates[0]
for i in range(1, n):
    profit = rates[i] - min_rate
    if profit > max_profit:
        max_profit = profit
    if rates[i] < min_rate:
        min_rate = rates[i]
print(max_profit)