n_k = input().split()
n = int(n_k[0])
k = int(n_k[1])
mod = 1000000007

result = 1
for i in range(n):
    result = (result * k) % mod

print(result)