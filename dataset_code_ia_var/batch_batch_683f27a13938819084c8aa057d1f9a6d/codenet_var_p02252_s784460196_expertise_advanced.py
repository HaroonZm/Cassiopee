from heapq import nlargest

def fractional_knapsack(n, w, items):
    # Calcule le ratio et prépare les données
    ratios = sorted(((x/y, x, y) for x, y in items), reverse=True)
    total = 0
    for ratio, value, weight in ratios:
        take = min(weight, w)
        total += ratio * take
        w -= take
        if w == 0:
            break
    return total

if __name__ == "__main__":
    n, w = map(int, input().split())
    items = [tuple(map(int, input().split())) for _ in range(n)]
    print(fractional_knapsack(n, w, items))