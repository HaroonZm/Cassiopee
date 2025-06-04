S = input()

max_k = 0
N = len(S)

for k in range(1, N//3 + 1):
    pattern = "J" * k + "O" * k + "I" * k
    if pattern in S:
        max_k = k

print(max_k)