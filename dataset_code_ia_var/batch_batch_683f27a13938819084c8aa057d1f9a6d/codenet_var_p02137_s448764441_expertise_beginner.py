n = int(input())
ans = 0
l = [10000, 5000, 1000, 500]

i = 0
while i < 4:
    ans = ans + (n // l[i]) * l[i]
    n = n % l[i]
    i = i + 1

print(ans)