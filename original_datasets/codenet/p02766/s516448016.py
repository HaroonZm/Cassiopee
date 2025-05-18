import math
N, K = input().split()

print(math.floor(math.log(int(N), int(K)))+1)