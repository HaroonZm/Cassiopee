import math

while True:
    n = int(input())
    if n == 0:
        break
    b = list(map(int, input().split()))
    # Total elements in a: n + 1
    # number of products: (n+1)*n/2 = length of b
    # a[0] is even, a[1..n] are odd
    # b contains all products a[i]*a[j], i<j

    # Sort b to get smallest products first
    b.sort()
    # The smallest product must be a[0]*a[1]
    # The products between odd elements start from b[n] because the first n products involve a[0]
    # To find a[0], use:
    # a[0] = gcd(b[0], b[1], b[2],...) but safer to pick a method:
    # For n odd integers a[1..n], products among them are b[n..]
    # a[0]*a[1] = b[0], a[0]*a[2] = b[1], a[0]*a[3] = b[2], ...
    # Then a[1]*a[2] = b[n], a[1]*a[3] = b[n+1], etc.

    # We can get a[0] by gcd of first n elements in b
    g = b[0]
    for i in range(1, n):
        g = math.gcd(g, b[i])
    a0 = g

    # Then get odd elements by dividing first n elements by a0
    odds = []
    for i in range(n):
        odds.append(b[i] // a0)
    odds.sort()

    print(a0)
    print(' '.join(str(x) for x in odds))