n_k = input().split(" ")
n = int(n_k[0])
k = int(n_k[1])
mod = 1000000007
result = pow(k, n, mod)
print(result)