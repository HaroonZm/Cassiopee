n = input()
plus = 0
minus = 0

for c in n:
    if c == "+":
        plus = plus + 1
    if c == "-":
        minus = minus + 1

result = plus - minus
print(result)