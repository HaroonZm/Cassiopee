from heapq import nlargest

def fractional_knapsack(items, capacity):
    # Compute value-to-weight ratio and use max-heap for efficiency
    heap = nlargest(len(items), ((v/w, w, v) for v, w in items))
    profit = 0
    for ratio, weight, value in heap:
        take = min(capacity, weight)
        profit += ratio * take
        capacity -= take
        if capacity == 0:
            break
    return profit

def main():
    N, W = map(int, input().split())
    items = [tuple(map(int, input().split())) for _ in range(N)]
    print(fractional_knapsack(items, W))

if __name__ == "__main__":
    main()