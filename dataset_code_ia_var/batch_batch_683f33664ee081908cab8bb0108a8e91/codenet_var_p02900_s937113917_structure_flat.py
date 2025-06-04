A, B = map(int, input().split())

a = A
A_dec = set()
i = 2
while i * i <= a:
    while a % i == 0:
        A_dec.add(i)
        a //= i
    i += 1
if a > 1:
    A_dec.add(a)

b = B
B_dec = set()
i = 2
while i * i <= b:
    while b % i == 0:
        B_dec.add(i)
        b //= i
    i += 1
if b > 1:
    B_dec.add(b)

ans = 1
for a in A_dec:
    if a in B_dec:
        ans += 1

print(ans)