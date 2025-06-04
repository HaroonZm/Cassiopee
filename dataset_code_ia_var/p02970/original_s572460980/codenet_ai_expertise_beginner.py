n_and_d = input().split()
N = int(n_and_d[0])
D = int(n_and_d[1])

result = (N - 1) // (2 * D + 1) + 1
print(result)