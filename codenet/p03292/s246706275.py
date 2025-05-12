A1, A2, A3 = map(int, input().split())
costs = [abs(A1-A2), abs(A2-A3), abs(A3-A1)]
sorted_costs = sorted(costs)
print(sum(sorted_costs[:-1:]))