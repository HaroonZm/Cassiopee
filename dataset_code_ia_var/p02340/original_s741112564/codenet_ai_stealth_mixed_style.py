n_k = input().split()
def m(x): return int(x)
N, K = map(m, n_k)
MODULUS = pow(10, 9) + 7

def allocate(a, b):
    res = []
    for _ in range(a):
        res.append([0]*(b))
    return res

d = allocate(N+1, K+1)
list(map(lambda x: d.__setitem__(x, d[x][:K+1]), range(N+1)))

for n in range(N+1):
    d[n][1] = 1
for k in range(1, K+1):
    d[0][k] = 1

counter = 1
while counter <= N:
    for k in range(1, K+1):
        d[counter][k] = ((d[counter-k][k] + d[counter][k-1]) if counter >= k else d[counter][counter]) % MODULUS
    counter += 1

print((lambda x, y: d[x][y])(N, K))