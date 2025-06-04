import math
N_K = input().split()
N = int(N_K[0])
K = int(N_K[1])
print(math.floor(math.log(N, K)) + 1)