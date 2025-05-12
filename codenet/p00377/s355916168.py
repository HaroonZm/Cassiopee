import math

N, C = list(map(int, input().split(' ')))
cakes = list(map(int, input().split(' ')))

num_cakes = sum(cakes)
mycake = math.ceil(num_cakes/(N+1))
print(mycake)