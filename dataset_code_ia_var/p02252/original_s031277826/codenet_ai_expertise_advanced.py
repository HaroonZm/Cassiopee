from heapq import heapify, heappop
from sys import stdin

def main():
    n, capacity = map(int, stdin.readline().split())
    items = [tuple(map(int, stdin.readline().split())) for _ in range(n)]
    
    # Fractional knapsack: sort by value/weight descending (using heap for O(NlogN))
    heap = [(-v/w, v, w) for v, w in items]
    heapify(heap)
    
    total_value = 0.0

    while heap and capacity > 0:
        value_per_weight, value, weight = heappop(heap)
        take = min(weight, capacity)
        total_value += take * -value_per_weight
        capacity -= take

    print(int(total_value) if total_value.is_integer() else total_value)

main()