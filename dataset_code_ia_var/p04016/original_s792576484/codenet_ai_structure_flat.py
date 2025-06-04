n = int(input())
s = int(input())
r = int(n ** 0.5)
found = False
b = 2
while b <= r + 1:
    m = n
    t = 0
    while m:
        t += m % b
        m //= b
    if t == s:
        print(b)
        found = True
        break
    b += 1
if not found:
    p = r - 1
    while p >= 1:
        q = s - p
        if p != 0:
            if (n - s) % p == 0:
                b = 1 + (n - s) // p
                if 1 <= p < b and 0 <= q < b:
                    print(b)
                    found = True
                    break
        p -= 1
if not found:
    if n == s:
        print(n + 1)
    else:
        print(-1)