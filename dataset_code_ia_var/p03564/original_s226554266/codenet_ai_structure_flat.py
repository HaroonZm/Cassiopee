N = int(input())
K = int(input())

val = 1
i = 0
while i < N:
    if val < K:
        val += val
    else:
        val += K
    i += 1

print(val)