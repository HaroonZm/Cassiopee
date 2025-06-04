n = int(input())
d = input().split()
for i in range(n):
    d[i] = int(d[i])

sum_d = 0
sum_dd = 0
for i in range(n):
    sum_d += d[i]
    sum_dd += d[i] * d[i]

result = (sum_d * sum_d - sum_dd) // 2
print(result)