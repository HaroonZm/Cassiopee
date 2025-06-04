n = int(input())
root = int(n ** 0.5) + 1
isPrime = [True] * (n + 3)

i = 4
while i < n + 3:
    isPrime[i] = False
    i += 2

ans = 0
prePrime = -1

i = 3
while i < n + 3:
    if isPrime[i]:
        if prePrime + 2 == i:
            ans += 2
        prePrime = i
        if i > root:
            i += 2
            continue
        j = i * i
        while j < n + 3:
            isPrime[j] = False
            j += i
    i += 2

print(ans)