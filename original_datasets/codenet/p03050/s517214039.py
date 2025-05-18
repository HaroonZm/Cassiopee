def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    divisors.sort()
    return divisors

N = int(input())
l = make_divisors(N)
g = 0
for c in l:
    rc = N//c - 1
    if (rc != 0):
        if (N % rc) == (N//rc):
            g+=rc
print(g)