import math

n = int(input())
i = 1
found = False

while i < 46298:
    if math.floor(i * 1.08) == n:
        print(i)
        found = True
        break
    i = i + 1

if not found:
    print(":(")