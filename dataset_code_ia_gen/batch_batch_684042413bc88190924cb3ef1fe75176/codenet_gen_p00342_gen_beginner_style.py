N = int(input())
a = list(map(int, input().split()))

max_value = -10**20
for i in range(N):
    for j in range(i+1, N):
        A = a[i]
        B = a[j]
        numerator = A + B
        for k in range(N):
            if k == i or k == j:
                continue
            for l in range(k+1, N):
                if l == i or l == j:
                    continue
                C = a[k]
                D = a[l]
                denominator = C - D
                if denominator != 0:
                    val = numerator / denominator
                    if val > max_value:
                        max_value = val
                # Also check the other order to get all combinations
                denominator = D - C
                if denominator != 0:
                    val = numerator / denominator
                    if val > max_value:
                        max_value = val

print(f"{max_value:.6f}")