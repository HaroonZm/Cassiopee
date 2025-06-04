n = int(input())
a = []
for i in range(n):
    num = int(input())
    a.append(num)

a.sort()
b = []
for num in a:
    b.append(num)

ans = 0

# Première méthode : commencer par le plus petit élément
first = a[0]
last = a[0]
tmp = 0
A = []
for num in a:
    A.append(num)
del A[0]
turn = True

while len(A) > 0:
    if len(A) == 1:
        tmp = tmp + max(abs(first - A[0]), abs(last - A[0]))
        break

    if turn:
        x = A[-2]
        y = A[-1]
    else:
        x = A[0]
        y = A[1]

    if abs(x - first) + abs(y - last) < abs(x - last) + abs(y - first):
        x, y = y, x

    tmp = tmp + abs(x - first) + abs(y - last)
    first = x
    last = y

    if turn:
        A.pop()
        A.pop()
    else:
        A.pop(0)
        A.pop(0)

    turn = not turn

ans = tmp

# Deuxième méthode : commencer par le plus grand élément
A = []
for num in b:
    A.append(num)
first = A[-1]
last = A[-1]
tmp = 0
A.pop()
turn = True

while len(A) > 0:
    if len(A) == 1:
        tmp = tmp + max(abs(first - A[0]), abs(last - A[0]))
        break

    if turn:
        x = A[0]
        y = A[1]
    else:
        x = A[-1]
        y = A[-2]

    if abs(x - first) + abs(y - last) < abs(x - last) + abs(y - first):
        x, y = y, x

    tmp = tmp + abs(x - first) + abs(y - last)
    first = x
    last = y

    if turn:
        A.pop(0)
        A.pop(0)
    else:
        A.pop()
        A.pop()

    turn = not turn

if tmp > ans:
    ans = tmp

print(ans)