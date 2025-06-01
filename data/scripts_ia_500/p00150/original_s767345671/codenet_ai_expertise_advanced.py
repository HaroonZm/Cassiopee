from bisect import bisect_right

P = [2] + [n for n in range(3, 10000, 2) if all(n % p for p in range(3, int(n**0.5) + 1, 2))]
P.reverse()

while True:
    n = int(input())
    if n == 0:
        break
    j = bisect_right(P[::-1], n)
    for i in range(j, len(P)-1):
        if P[i] - 2 == P[i+1]:
            print(P[i+1], P[i])
            break