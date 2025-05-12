n = int(input())

tn = n
t = []
for i in range(2, int(n ** 0.5) + 1):
    while n % i == 0:
        n //= i
        t.append(i)

if n != 1:
    t.append(n)

print("{}: {}".format(tn, " ".join(map(str, t))))