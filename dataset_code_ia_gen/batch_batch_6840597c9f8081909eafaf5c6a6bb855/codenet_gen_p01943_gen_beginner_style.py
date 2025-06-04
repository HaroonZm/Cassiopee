N,K = input().split()
N = int(N)
K = float(K)
S = []
for _ in range(N):
    S.append(float(input()))

max_length = 0
for start in range(N):
    product = 1.0
    for end in range(start, N):
        product *= S[end]
        if product > K:
            break
        length = end - start + 1
        if length > max_length:
            max_length = length

print(max_length)