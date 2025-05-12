N = int(input())
lst = [int(input()) for _ in range(N)]
max_ = max(lst)
divisors = []
d = 0

for i in range(1, int(max_**0.5) + 1):
    if max_ % i == 0:
        divisors.append(i)
        divisors.append(max_ // i)
divisors.sort()

for i in sorted(lst):
    for divisor in divisors:
        if i <= divisor:
            d += divisor - i
            break

print(d)