xx, yy = list(map(int, input().split()))
fib = [1, 1]
a = 0
while a < 10000000:
    a = fib[-1] + fib[-2]
    fib += [a]
area = [[0, 0, 1]]
x, y = 0, 0
f1 = 0
f2 = 1
for n in range(1, len(fib)):
    a = fib[n]
    if n % 4 == 1:
        area += [[x + f2, y + f1, a]]
    elif n % 4 == 2:
        area += [[x - f1, y + a, a]]
    elif n % 4 == 3:
        area += [[x - a, y, a]]
    elif n % 4 == 0:
        area += [[x, y - f2, a]]
    f1 = f2
    f2 = a
    x, y = area[-1][0:2]
for n, floor in enumerate(area):
    x, y, a = floor
    if x <= xx < x + a and y - a < yy <= y:
        print(n % 3 + 1)
        break