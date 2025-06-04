x = int(input())
l = int((2 * x) ** 0.5)
while l * (l + 1) < 2 * x:
    l = l + 1
print(l)