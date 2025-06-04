while True:
    K = int(input())
    if K == 0:
        break
    values = list(map(int, input().split()))
    # total sum of pairs is sum of ci
    total_pairs_sum = sum(values)
    # sum of all cakes = 2 * total_pairs_sum / (K * (K-1))
    total_cakes_sum = 2 * total_pairs_sum // (K * (K - 1))
    print(total_cakes_sum)