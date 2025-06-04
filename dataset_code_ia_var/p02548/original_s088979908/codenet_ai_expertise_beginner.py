n = int(input())

result = 0

for a in range(1, n):
    b_max = n // a
    if n % a == 0:
        b_max = b_max - 1
    if b_max > 0:
        result = result + b_max

print(result)