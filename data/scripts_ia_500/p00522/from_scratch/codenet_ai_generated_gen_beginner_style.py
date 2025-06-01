M, N = map(int, input().split())
prices = [int(input()) for _ in range(M)]
boxes = [tuple(map(int, input().split())) for _ in range(N)]

prices.sort(reverse=True)

max_profit = 0
from itertools import combinations

# On considère toutes les combinaisons de boîtes (moins optimisé)
for select in range(1, N+1):
    for combi in combinations(range(N), select):
        total_capacity = sum(boxes[i][0] for i in combi)
        total_cost = sum(boxes[i][1] for i in combi)
        # On prend les M meilleurs manjuu possibles à mettre dans les boîtes
        # En réalité, on ne peut pas mettre plus de total_capacity manjuu
        taken = prices[:min(total_capacity, M)]
        total_price = sum(taken)
        profit = total_price - total_cost
        if profit > max_profit:
            max_profit = profit

print(max_profit)