inputs = []
for _ in range(3):
    inputs.append(input())
min1 = min(inputs)

min2 = min([input() for _ in range(2)])

print(min1 + min2 - 50)