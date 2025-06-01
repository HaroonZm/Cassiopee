from itertools import permutations

def compute_frustration(order, a, w):
    n = len(order)
    total = 0
    for i in range(n):
        sage = order[i]
        left = order[(i - 1) % n]
        right = order[(i + 1) % n]
        if a[sage] == 0:  # right-handed
            # frustration if left-handed sage on right
            if a[right] == 1:
                total += w[sage]
        else:  # left-handed
            # frustration if right-handed sage on left
            if a[left] == 0:
                total += w[sage]
    return total

def main():
    N = int(input())
    a = list(map(int, input().split()))
    w = list(map(int, input().split()))
    sages = list(range(N))
    min_frustration = float('inf')
    for order in permutations(sages):
        f = compute_frustration(order, a, w)
        if f < min_frustration:
            min_frustration = f
    print(min_frustration)

if __name__ == "__main__":
    main()