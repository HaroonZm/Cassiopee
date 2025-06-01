n = int(input())
debt = 100000
for _ in range(n):
    debt = int(((debt * 1.05 + 999) // 1000) * 1000)
print(debt)