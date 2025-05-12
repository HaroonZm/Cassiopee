def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    # divisors.sort()
    return divisors

X = {}
N = int(input())

for i in make_divisors(N-1):
    X[i] = 1

for i in make_divisors(N):
    hoge = N
    if i == 1:
        continue
    while hoge % i == 0:
        hoge //= i
    if hoge % i == 1:
        X[i] = 1
    else:
        X[i] = 0

"""
for k,i in X.items():
    if i >= 1:
        print(k)
"""
print(sum(X.values())-1)