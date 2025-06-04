from math import factorial

def comb(n, r):
    return factorial(n) // (factorial(r) * factorial(n - r))

N, A, B = map(int, input().split())
V = list(map(int, input().split()))
V.sort(reverse=True)

sums = []
for i in range(1, N + 1):
    s = sum(V[:i])
    avg = s / i
    sums.append(avg)

max_avg = 0
for i in range(A - 1, B):
    if sums[i] > max_avg:
        max_avg = sums[i]

count = 0
for size in range(A, B + 1):
    s = sum(V[:size])
    avg = s / size
    if avg == max_avg:
        min_value = V[size - 1]
        total = V.count(min_value)
        chosen = V[:size].count(min_value)
        count += comb(total, chosen)

print(max_avg)
print(count)