def gcd(a, b):
    while b != 0:
        r = a % b
        a = b
        b = r
    return a

while True:
    n = int(input())
    if n == 0:
        break
    a = list(map(int, input().split()))
    even = []
    odd = []
    for x in a:
        if x % 2 == 0:
            even.append(x)
        else:
            odd.append(x)
    even.sort()
    odd.sort()
    e1 = even[0]
    e2 = even[1]
    o1 = odd[0]
    g = gcd(e1, o1)
    e1 = e1 // g
    o1 = o1 // g
    g2 = gcd(e2, o1)
    e2 = e2 // g2
    o1 = o1 // g2
    ans = int((e1 * e2) ** 0.5)
    print(ans)
    res = []
    for x in even:
        res.append(x // ans)
    print(*res)